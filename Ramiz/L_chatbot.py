import requests
import json
import os
from dotenv import load_dotenv
from tkinter import Tk, Text, Entry, Button, Scrollbar, END, messagebox, DISABLED, NORMAL
import threading

# Load environment variables from .env file
load_dotenv()

# --- Configuration Loaded from .env ---
AI_PROVIDER = os.getenv("AI_PROVIDER")
BASE_URL = os.getenv("DEEPSEEK_BASE_URL")
API_URL = BASE_URL + "/chat/completions"
API_KEY = os.getenv("DEEPSEEK_API_KEY")
MODEL_NAME = os.getenv("DEEPSEEK_MODEL")
HISTORY_FILE = "chat_history.json" 

# --- New Context Management Constant ---
MAX_CONTEXT_MESSAGES = 18 

if not API_KEY or not MODEL_NAME or not BASE_URL:
    print("FATAL ERROR: Essential environment variables not set in .env file.")
    exit()

# ----------------------------------------
# 1. API Logic 
# ----------------------------------------

def get_deepseek_response(messages_history, is_summary_request=False):
    """
    Sends a request to DeepSeek with the message history.
    If is_summary_request is True, it uses a specific prompt for summarization.
    """
    
    headers = {
        "Authorization": f"Bearer {API_KEY}", 
        "Content-Type": "application/json"
    }
    
    data = {
        "model": MODEL_NAME,
        "messages": messages_history,
        "stream": False,
        "temperature": 0.3 if is_summary_request else 0.7 
    }
    
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data), timeout=45)
        response.raise_for_status()
        
        response_data = response.json()
        
        if response_data and 'choices' in response_data and len(response_data['choices']) > 0:
            return response_data['choices'][0]['message'] 
        else:
            return {"role": "system", "content": "No response received from the model."}

    except requests.exceptions.HTTPError as e:
        return {"role": "system", "content": f"HTTP Error: {e}. Please check your API Key and Base URL."}
    except requests.exceptions.Timeout:
        return {"role": "system", "content": "Connection Timeout: The API took too long to respond."}
    except requests.exceptions.RequestException as e:
        return {"role": "system", "content": f"Communication Error: {e}"}
    except Exception as e:
        return {"role": "system", "content": f"Unknown Error: {e}"}


# ----------------------------------------
# 2. Tkinter UI Logic (With Intelligent Summarization)
# ----------------------------------------

class ChatBotUI:
    def __init__(self, master):
        self.master = master
        master.title(f"{AI_PROVIDER.upper()} Intelligent Chat")
        master.geometry("500x600")

        # --- Chat History Storage ---
        self.chat_history = [] 
        self.default_system_message = {"role": "system", "content": "You are a helpful and creative assistant named ChatBot. You are powered by " + AI_PROVIDER + "."}
        
        # Register save function to run when the application closes
        master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.load_history() 

        # --- UI Setup ---
        self.chat_display = Text(master, wrap='word', state=DISABLED, bg="#f0f0f0", font=('Arial', 10))
        self.scrollbar = Scrollbar(master, command=self.chat_display.yview)
        self.chat_display.config(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.chat_display.grid(row=0, column=0, columnspan=1, sticky='nsew', padx=5, pady=5)
        
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        self.user_input = Entry(master, font=('Arial', 12))
        self.user_input.grid(row=1, column=0, sticky='ew', padx=5, pady=(0, 5))
        self.user_input.bind("<Return>", self.send_message_event)

        self.send_button = Button(master, text="Send", command=self.send_message, bg="#4CAF50", fg="white", font=('Arial', 10, 'bold'))
        self.send_button.grid(row=1, column=1, sticky='e', padx=5, pady=(0, 5))
        
        self.refresh_display()

    # --- History I/O ---

    def load_history(self):
        """Loads chat history from the JSON file."""
        if os.path.exists(HISTORY_FILE):
            try:
                with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                    loaded_messages = json.load(f)
                    
                    last_system_message = next((msg for msg in reversed(loaded_messages) if msg["role"] == "system"), self.default_system_message)
                    conversation_messages = [msg for msg in loaded_messages if msg["role"] != "system"]
                    
                    self.chat_history = [last_system_message] + conversation_messages
                    
            except Exception as e:
                messagebox.showerror("History Load Error", f"Could not load chat history: {e}")
                self.chat_history = [self.default_system_message] 
        else:
            self.chat_history = [self.default_system_message]

    def save_history(self):
        """Saves the current chat history to the JSON file."""
        try:
            with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.chat_history, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"History Save Error: Could not save chat history: {e}") 

    def on_closing(self):
        """
        Runs the final, synchronous summarization before closing.
        """
        # --- NEW LOGIC: Synchronous Final Summarization ---
        self.summarize_all_on_exit()
        # --------------------------------------------------
        
        self.master.destroy()
        
    def refresh_display(self):
        """Clears the chat display and redraws the content based on self.chat_history."""
        self.chat_display.config(state=NORMAL)
        self.chat_display.delete('1.0', END)
        
        conversation_count = sum(1 for msg in self.chat_history if msg["role"] != "system")
        
        if conversation_count > 0:
            summary_content = self.chat_history[0]['content']
            self.display_message(f"--- Loaded Context ({conversation_count} messages) ---\nContext: {summary_content[:150]}...", "system", is_new=False)
            
            for msg in self.chat_history[1:]:
                self.display_message(msg['content'], msg['role'], is_new=False)
        else:
            self.display_message(f"--- Welcome to {AI_PROVIDER.upper()} ChatBot! ---", "system", is_new=False)
            self.display_message("Type your message below and press Enter or the Send button.", "system", is_new=False)
            
        self.chat_display.config(state=DISABLED)

    def display_message(self, message, sender, is_new=True):
        """
        Displays a message and optionally adds it to history.
        """
        self.chat_display.config(state=NORMAL)
        
        if sender == "user":
            prefix = "You: "
            tag = "user_tag"
            color = "blue"
        elif sender == "assistant":
            prefix = "Bot: "
            tag = "bot_tag"
            color = "black"
        else: 
            prefix = ""
            tag = "system_tag"
            color = "gray"
        
        self.chat_display.insert(END, f"{prefix}{message}\n\n", tag)
        self.chat_display.tag_config(tag, foreground=color)
        
        self.chat_display.see(END)
        self.chat_display.config(state=DISABLED)

        if is_new and sender in ["user", "assistant"]:
            self.chat_history.append({"role": sender, "content": message})

    # --- NEW: Synchronous Summarization on Exit ---
    def summarize_all_on_exit(self):
        """
        Synchronously summarizes the entire chat history and updates the system context.
        This function is called only when the application is closing.
        """
        # Only summarize if there are conversation messages (history length > 1)
        if len(self.chat_history) > 1:
            print("\n[CLEANUP] Starting final chat history summarization before closing...")
            
            # Temporarily disable UI interaction and show status
            self.user_input.config(state=DISABLED)
            self.send_button.config(state=DISABLED, text="Cleaning Up...")
            self.display_message("--- Performing Final Context Summarization... Please wait. ---", "system", is_new=False)
            self.master.update() # Force UI refresh

            messages_to_summarize = self.chat_history[1:] 
            
            summary_prompt = {
                "role": "user",
                "content": ("You are a summarization engine. Condense the entire following conversation history into a single, concise 'system message'. ONLY include key facts, user preferences, and explicit instructions. Omit all small talk, greetings, and unnecessary filler. The final output must be ready to be used as a new system instruction. DO NOT add greetings or intros.")
            }
            
            # Send the existing system message + conversation history + the summary prompt
            messages_for_api = [self.chat_history[0]] + messages_to_summarize + [summary_prompt]

            # Synchronous API call
            summary_object = get_deepseek_response(messages_for_api, is_summary_request=True)
            
            new_summary_content = summary_object.get("content")
            
            if summary_object.get("role") == "system":
                print(f"[CLEANUP ERROR] Failed to summarize: {new_summary_content}. Saving unsummarized history.")
                self.display_message(f"--- ERROR: Final summarization failed. Saving full history. ---", "system", is_new=False)
            else:
                # 1. Create the new system message 
                new_system_message = {
                    "role": "system",
                    "content": f"{self.default_system_message['content']} \n\n**Conversation Summary:** {new_summary_content}"
                }
                
                # 2. Rebuild history: Only the new system message remains
                self.chat_history = [new_system_message]
                
                print("[CLEANUP SUCCESS] History summarized and compressed successfully. Only the final context is saved.")
                self.display_message(f"--- SUCCESS: Context compressed to final summary. ---", "system", is_new=False)

        # Always save (either the full history or the new summarized history)
        self.save_history()


    # --- Summarization Logic (Mid-Chat) ---

    def request_summary_and_update_history(self):
        """
        (Asynchronous) Runs the mid-chat summarization API call.
        """
        # ... (Existing logic for mid-chat summarization remains the same)
        messages_to_summarize = self.chat_history[1:] 
        
        summary_prompt = {
            "role": "user",
            "content": (
                "You are a summarization engine. Your task is to condense the provided conversation history into a single, concise 'system message'. "
                "This summary MUST only contain key facts, instructions, user preferences, names, and explicit constraints. "
                "Delete all unnecessary small talk, greetings, filler words, and repetitive questions. "
                "The final output must be ready to be used as a new system instruction. DO NOT add greetings or intros."
            )
        }
        
        messages_for_api = [self.chat_history[0]] + messages_to_summarize + [summary_prompt]

        # Get the summary from the API
        summary_object = get_deepseek_response(messages_for_api, is_summary_request=True)
        
        # Safely update the UI from the background thread
        self.master.after(0, self.apply_summary_update, summary_object)

    def apply_summary_update(self, summary_object):
        """
        Replaces old conversation history with the new summary.
        """
        # ... (Existing logic remains the same)
        new_summary_content = summary_object.get("content")
        
        if summary_object.get("role") == "system":
            self.display_message(f"Error during mid-chat summarization: {new_summary_content}", "system")
        else:
            new_system_message = {
                "role": "system",
                "content": f"{self.default_system_message['content']} \n\n**Conversation Summary:** {new_summary_content}"
            }
            
            MESSAGES_TO_KEEP = 6
            recent_messages = self.chat_history[-(MESSAGES_TO_KEEP):]
            
            self.chat_history = [new_system_message] + recent_messages
            
            self.display_message(f"--- Context Summarized Successfully! (Kept {MESSAGES_TO_KEEP} recent messages) ---", "system")
            self.save_history() 

        self.user_input.config(state=NORMAL)
        self.send_button.config(state=NORMAL, text="Send")
        self.user_input.focus_set()


    # --- Message Sending ---

    def send_message_event(self, event):
        self.send_message()
    
    def send_message(self):
        user_text = self.user_input.get().strip()
        self.user_input.delete(0, END)

        if not user_text:
            return

        self.display_message(user_text, "user")
        
        self.user_input.config(state=DISABLED)
        self.send_button.config(state=DISABLED, text="Thinking...")

        # Check if mid-chat summarization is needed (for performance)
        conversation_count = sum(1 for msg in self.chat_history if msg["role"] != "system")
        
        if conversation_count >= MAX_CONTEXT_MESSAGES:
            self.display_message(f"--- History too long ({conversation_count} messages). Starting intelligent summarization... ---", "system")
            thread = threading.Thread(target=self.request_summary_and_update_history)
            thread.start()
        else:
            thread = threading.Thread(target=self.get_bot_response_threaded)
            thread.start()

    def get_bot_response_threaded(self):
        """
        Fetches the bot response using the complete (and possibly compressed) chat history.
        """
        bot_message_object = get_deepseek_response(self.chat_history)
        
        self.master.after(0, self.update_ui_after_response, bot_message_object)

    def update_ui_after_response(self, bot_message_object):
        """
        Updates the UI elements after the bot response is received.
        """
        role = bot_message_object.get("role", "system")
        content = bot_message_object.get("content", "Error: No content received.")
        
        self.display_message(content, role)
        
        self.user_input.config(state=NORMAL)
        self.send_button.config(state=NORMAL, text="Send")
        self.user_input.focus_set()


if __name__ == "__main__":
    root = Tk()
    app = ChatBotUI(root)
    root.mainloop()