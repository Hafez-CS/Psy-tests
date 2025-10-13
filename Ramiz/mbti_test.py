import tkinter as tk
from tkinter import messagebox, ttk
from functools import partial

# --- 1. QUESTIONS AND DATA STRUCTURE ---
# Each question contains: [Question Text, Option A Text, Option B Text, Trait for A, Trait for B]
QUESTIONS = [
    # E/I - Extraversion vs. Introversion (15 Questions)
    ["At a party, you...", "I get to know many new people.", "I mostly talk to people I already know.", "E", "I"],
    ["When you feel low on energy, you prefer to...", "Go out and spend time with others.", "Be alone to recharge.", "E", "I"],
    ["In conversations, you tend to...", "Talk to think (think out loud).", "Think first, then speak.", "E", "I"],
    ["Would you rather have a busy day with many activities or a quiet, focused day?", "Busy and varied.", "Quiet and focused.", "E", "I"],
    ["Regarding a new project, you...", "Act quickly and make adjustments as you go.", "Spend a lot of time thinking and planning before starting.", "E", "I"],
    ["Others see you as a person who is...", "Talkative and social.", "Quiet and reserved.", "E", "I"],
    ["Do you enjoy unexpected phone calls?", "Yes, most of the time.", "No, I prefer they send a message.", "E", "I"],
    ["Your focus is more on...", "Your surroundings and external events.", "Your own internal thoughts and feelings.", "E", "I"],
    ["Do you like having many different activities?", "Yes, the more the better.", "No, I focus deeply on just a few things.", "E", "I"],
    ["When you see someone, you...", "Quickly say hello and start a conversation.", "Wait for them to start the conversation first.", "E", "I"],
    ["You are more drawn to...", "Expressive and enthusiastic people.", "Calm and thoughtful people.", "E", "I"],
    ["Do you find it hard to be alone for a long time?", "Yes, usually.", "No, I enjoy it.", "E", "I"],
    ["You enjoy working in...", "A noisy and bustling office.", "A quiet environment with no distractions.", "E", "I"],
    ["Do you consider yourself more of an 'action-oriented' person or a 'thought-oriented' person?", "Action-oriented.", "Thought-oriented.", "E", "I"],
    ["In a group, you are usually the first to...", "Ask a question or share an opinion.", "Listen to what others are saying.", "E", "I"],
    
    # S/N - Sensing vs. Intuition (15 Questions)
    ["When describing an event, you...", "State all the objective, real details accurately.", "Refer to the big picture and the meaning of the event.", "S", "N"],
    ["What part of a story do you pay more attention to?", "The current events and how they happened.", "The future consequences and possibilities.", "S", "N"],
    ["You are more engaged with...", "Facts and proven realities.", "Ideas and new possibilities.", "S", "N"],
    ["Which is more difficult for you?", "Doing repetitive, detailed tasks.", "Thinking about abstract and theoretical concepts.", "S", "N"],
    ["Which do you prefer?", "Step-by-step and clear instructions.", "Working with a general goal and freedom in how to achieve it.", "S", "N"],
    ["Do you tend to talk about details?", "Yes, most of the time.", "No, I get bored with long, detailed conversations.", "S", "N"],
    ["You pay more attention to...", "What 'is'.", "What 'could be'.", "S", "N"],
    ["When solving a problem, you...", "Think of tried and proven solutions.", "Look for innovative and unprecedented solutions.", "S", "N"],
    ["You are more interested in...", "Practical and applicable work.", "Theoretical and conceptual work.", "S", "N"],
    ["When reading a book, you...", "Focus more on the main storyline.", "Are constantly reading between the lines and finding hidden meanings.", "S", "N"],
    ["When faced with change, you...", "Feel uncomfortable because it disrupts the existing order.", "Get excited because it creates new possibilities.", "S", "N"],
    ["Which is more important to you?", "Being realistic and cautious.", "Being imaginative and bold.", "S", "N"],
    ["You tend to...", "Learn from past experiences.", "Focus on future possibilities.", "S", "N"],
    ["When listening to others, you...", "Pay attention to what they say.", "Pay attention to what they *mean*.", "S", "N"],
    ["Do you enjoy memorizing specific details and facts?", "Yes, it's easy and useful for me.", "No, it's boring.", "S", "N"],
    
    # T/F - Thinking vs. Feeling (15 Questions)
    ["When making a decision, you mostly act based on...", "Logical analysis and objective results.", "Considering values and the impact of the decision on others.", "T", "F"],
    ["Which is worse?", "To be illogical.", "To be cruel.", "T", "F"],
    ["Are you comfortable criticizing others (if necessary)?", "Yes, if the criticism is constructive.", "No, I worry about hurting their feelings.", "T", "F"],
    ["What is more important to you at work?", "Justice and fairness (based on rules and logic).", "Empathy and compassion (based on the individual's situation).", "T", "F"],
    ["When you face a problem, you first...", "Try to find its logical cause and solution.", "Try to make sure everyone is emotionally okay.", "T", "F"],
    ["You see yourself as a person who is...", "Decisive and firm.", "Compassionate and kind.", "T", "F"],
    ["Do you think it's okay to show emotion at work?", "No, the workplace should be objective and logical.", "Yes, it's a sign of being human.", "T", "F"],
    ["Which is more admirable?", "The ability to defend a tough, unpopular position.", "The ability to create agreement and harmony among people.", "T", "F"],
    ["Do you tend to...", "Analyze discussions to reach a conclusion.", "Manage the emotional aspect of discussions.", "T", "F"],
    ["Would you rather be...", "Smart and competent.", "Warm and well-liked.", "T", "F"],
    ["Do you get angry more easily or sad?", "Angry.", "Sad.", "T", "F"],
    ["How do you think people see you?", "As a clear-thinking and logical person.", "As a warm and empathetic person.", "T", "F"],
    ["In evaluating others' performance, you...", "Apply the same standards and criteria to everyone.", "Consider the individual's personal circumstances and motives.", "T", "F"],
    ["For you, a tough decision is more of...", "A logical challenge to be solved.", "An emotional conflict to be managed.", "T", "F"],
    ["Are you someone who 'says no easily'?", "Yes, if I have a logical reason.", "No, I'm afraid of disappointing others.", "T", "F"],

    # J/P - Judging vs. Perceiving (15 Questions)
    ["Are your plans...", "Set in advance, and you prefer to stick to them.", "Often changing, and you are flexible.", "J", "P"],
    ["When you have an important task, do you prefer to...", "Finish the task first, then relax.", "Wait until the last minute to make it more exciting.", "J", "P"],
    ["You enjoy situations that are...", "Organized and structured.", "Spontaneous and unexpected.", "J", "P"],
    ["Do you find having many options...", "Stressful, because it makes decisions harder.", "Appealing, because it creates new possibilities.", "J", "P"],
    ["In a work environment, you prefer to have...", "Clear deadlines and rules.", "Freedom and flexibility to do your tasks.", "J", "P"],
    ["When you go on vacation, you...", "Book all the details (flight, hotel, activities) in advance.", "Book only a few main things and leave the rest to the moment.", "J", "P"],
    ["Do you tend to...", "Quickly finish unfinished tasks to get them off your mind.", "Keep tasks open to allow for changes and improvements.", "J", "P"],
    ["What part of a project do you focus on more?", "The execution and completion.", "The start and information gathering.", "J", "P"],
    ["When organizing your life, you prefer to...", "Use and rely on clear lists and schedules.", "Keep your schedule open and flexible.", "J", "P"],
    ["Do delays or cancellations in your plans upset you?", "Yes, my order is disrupted.", "No, it's not a problem, and I can find other things to do.", "J", "P"],
    ["If you have free time, you prefer to...", "Organize your home and take care of pending matters.", "Explore and wander around without a specific goal.", "J", "P"],
    ["In decision-making, do you...", "Quickly reach a conclusion.", "Like to keep gathering information until the last minute.", "J", "P"],
    ["Do you feel that 'planning' is vital for your life?", "Yes.", "No.", "J", "P"],
    ["Which is more enjoyable for you?", "A completely planned and organized day.", "A day full of surprises and sudden events.", "J", "P"],
    ["Do you prefer your belongings to be...", "Always in their specific, organized place.", "Always within reach, even if they are a bit messy.", "J", "P"],
]

# --- 2. STATE AND SCORING ---
user_answers = [0] * len(QUESTIONS)
current_q_index = 0
scores = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}

# Dark Mode Colors
BG_COLOR = '#2C2C2C'
FG_COLOR = '#E0E0E0'
ACCENT_COLOR = '#3984E2'
SELECTED_COLOR = '#3CB371'
BUTTON_HOVER_COLOR = '#3C3C3C'

# --- 3. CORE FUNCTIONS (ALGORITHM & NAVIGATION) ---

def select_option(choice):
    """Saves the user's choice and updates button appearance."""
    user_answers[current_q_index] = choice
    
    # Update button appearance
    if choice == 1:
        btn_a.config(bg=SELECTED_COLOR, fg='white')
        btn_b.config(bg=BG_COLOR, fg=FG_COLOR)
    else:
        btn_a.config(bg=BG_COLOR, fg=FG_COLOR)
        btn_b.config(bg=SELECTED_COLOR, fg='white')

def go_previous():
    """Moves to the previous question."""
    global current_q_index
    if current_q_index > 0:
        current_q_index -= 1
        # Access the progress bar (first child of main_frame)
        progress_bar = root.winfo_children()[0].winfo_children()[0] 
        display_question(progress_bar)
        
def go_next():
    """Moves to the next question or finishes the test."""
    global current_q_index
    
    # Ensure an option is selected before moving on
    if user_answers[current_q_index] == 0:
        messagebox.showerror("Error", "Please select an option to proceed.")
        return
        
    if current_q_index < len(QUESTIONS) - 1:
        current_q_index += 1
        progress_bar = root.winfo_children()[0].winfo_children()[0]
        display_question(progress_bar)
    else:
        # End of test
        calculate_and_show_result()
        
def handle_enter_key(event):
    """Handles the Enter key press."""
    # This prevents the Enter key from firing if the user hasn't selected an option
    if user_answers[current_q_index] != 0:
        go_next()

def display_question(progress_bar):
    """Displays the current question and updates navigation buttons."""
    
    question_data = QUESTIONS[current_q_index]
    
    # Update progress bar
    progress_bar['value'] = (current_q_index / len(QUESTIONS)) * 100
    
    # Update question text
    question_text = f"Question {current_q_index + 1} of {len(QUESTIONS)}:\n\n{question_data[0]}"
    question_label.config(text=question_text)
    
    # Update option button texts
    btn_a.config(text=f"A: {question_data[1]}")
    btn_b.config(text=f"B: {question_data[2]}")
    
    # Update button appearance based on stored answer
    selected_choice = user_answers[current_q_index]
    if selected_choice == 1:
        btn_a.config(bg=SELECTED_COLOR, fg='white')
        btn_b.config(bg=BG_COLOR, fg=FG_COLOR)
    elif selected_choice == 2:
        btn_a.config(bg=BG_COLOR, fg=FG_COLOR)
        btn_b.config(bg=SELECTED_COLOR, fg='white')
    else:
        # No answer yet
        btn_a.config(bg=BG_COLOR, fg=FG_COLOR)
        btn_b.config(bg=BG_COLOR, fg=FG_COLOR)

    # Manage Previous button state
    btn_prev.config(state=tk.NORMAL, bg='#555555') if current_q_index > 0 else btn_prev.config(state=tk.DISABLED, bg='#3C3C3C')

    # Manage Next button text/color
    btn_next.config(text="Show Result", bg='#FF4500') if current_q_index == len(QUESTIONS) - 1 else btn_next.config(text="Next Question »", bg=ACCENT_COLOR)

def calculate_mbti_scores():
    """Calculates the final scores and returns the MBTI type."""
    global scores
    # Reset and recalculate scores
    scores = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}

    for i, choice in enumerate(user_answers):
        if choice == 1:
            trait = QUESTIONS[i][3]
            scores[trait] += 1
        elif choice == 2:
            trait = QUESTIONS[i][4]
            scores[trait] += 1
    
    # Determine final type (using >= for ties)
    dim1 = 'E' if scores['E'] >= scores['I'] else 'I'
    dim2 = 'S' if scores['S'] >= scores['N'] else 'N'
    dim3 = 'T' if scores['T'] >= scores['F'] else 'F'
    dim4 = 'J' if scores['J'] >= scores['P'] else 'P'
    
    return dim1 + dim2 + dim3 + dim4

def calculate_and_show_result():
    """Calculates scores and opens the modern result window."""
    mbti_result = calculate_mbti_scores()
    # root.withdraw() # CHANGED: Do not withdraw. Instead, disable and grab focus.
    root.attributes('-disabled', True) # Disable the main window
    show_mbti_result_window(mbti_result)

def show_mbti_result_window(mbti_type):
    """Displays results with visual progress bars (FIXED TclError and Focus)."""
    
    result_window = tk.Toplevel(root)
    result_window.title("Your MBTI Result")
    result_window.geometry("550x500")
    result_window.config(bg=BG_COLOR)
    result_window.transient(root)
    result_window.resizable(False, False)

    # Key Fix: grab_set ensures this window is modal and receives all events
    result_window.grab_set() 
    result_window.lift()
    
    # Handle closing the result window (closes the entire app and re-enables main window)
    def on_result_close():
        result_window.grab_release()
        root.attributes('-disabled', False) # Re-enable main window (though we close the app right after)
        root.destroy()
        
    result_window.protocol("WM_DELETE_WINDOW", on_result_close)
    
    # Styling for Progress Bars (standard style name to avoid TclError)
    style = ttk.Style(result_window)
    style.theme_use('default')
    style.configure("Custom.Horizontal.TProgressbar", troughcolor='#555555', background=ACCENT_COLOR, thickness=20)
    
    result_frame = tk.Frame(result_window, padx=30, pady=30, bg=BG_COLOR)
    result_frame.pack(fill='both', expand=True)

    # Final Type Display
    tk.Label(result_frame, text="Your Personality Type is:", 
             bg=BG_COLOR, fg=FG_COLOR, font=('Helvetica', 14)).pack(pady=(10, 5))
    
    tk.Label(result_frame, text=mbti_type, 
             bg=BG_COLOR, fg=SELECTED_COLOR, font=('Helvetica', 36, 'bold')).pack(pady=(0, 30))

    # Dichotomies Data: (Label, Right Trait, Left Trait)
    dichotomies = [
        ("E-I (Energy)", 'E', 'I'),
        ("S-N (Information)", 'S', 'N'),
        ("T-F (Decision)", 'T', 'F'),
        ("J-P (Lifestyle)", 'J', 'P'),
    ]
    
    total_questions_per_dichotomy = 15 

    for label_text, trait1, trait2 in dichotomies:
        score1 = scores[trait1] # Right Trait (E, S, T, J)
        score2 = scores[trait2] # Left Trait (I, N, F, P)
        
        # Label for the dichotomy
        tk.Label(result_frame, text=label_text, bg=BG_COLOR, fg=FG_COLOR, 
                 font=('Helvetica', 10, 'bold')).pack(pady=(15, 5), anchor='w')
        
        bar_container = tk.Frame(result_frame, bg=BG_COLOR)
        bar_container.pack(fill='x')
        
        # Left Label (Trait 2: I, N, F, P)
        label_left_text = f"{trait2}: {score2}"
        tk.Label(bar_container, text=label_left_text, bg=BG_COLOR, fg=FG_COLOR).pack(side=tk.LEFT, padx=5)
        
        # Progress Bar
        progress = ttk.Progressbar(bar_container, orient="horizontal", length=300, 
                                   mode="determinate", maximum=total_questions_per_dichotomy,
                                   style="Custom.Horizontal.TProgressbar")
        
        # Set the bar's value based on the score of the LEFT trait (Trait 2)
        progress['value'] = score2 
        
        progress.pack(side=tk.LEFT, fill='x', expand=True, padx=10)
        
        # Right Label (Trait 1: E, S, T, J)
        label_right_text = f"{trait1}: {score1}"
        tk.Label(bar_container, text=label_right_text, bg=BG_COLOR, fg=FG_COLOR).pack(side=tk.RIGHT, padx=5)

    # Close button
    tk.Button(result_frame, text="Close Test", command=on_result_close, 
              font=('Helvetica', 11, 'bold'), bg='#CC0000', fg='white', 
              padx=15, pady=8, borderwidth=0, relief=tk.FLAT).pack(pady=40)

# --- 4. UI SETUP ---

def create_ui():
    """Main UI setup and Tkinter loop execution."""
    global root, question_label, btn_a, btn_b, nav_frame, btn_prev, btn_next
    
    root = tk.Tk()
    root.title("MBTI Personality Test")
    root.geometry("700x550")
    root.resizable(False, False)
    root.config(bg=BG_COLOR)
    
    # Bind the Enter key to the go_next function
    root.bind('<Return>', handle_enter_key) 

    # Frame for organization
    main_frame = tk.Frame(root, padx=30, pady=30, bg=BG_COLOR)
    main_frame.pack(fill='both', expand=True)
    
    # Progress Bar Styling
    style = ttk.Style(root)
    style.theme_use('default')
    style.configure("TProgressbar", troughcolor=BG_COLOR, background=ACCENT_COLOR, thickness=10)

    progress_bar = ttk.Progressbar(main_frame, orient="horizontal", length=600, 
                                   mode="determinate", style="TProgressbar")
    progress_bar.pack(pady=(0, 20))
    
    # Question Label
    question_label = tk.Label(main_frame, text="", wraplength=600, justify=tk.LEFT, 
                              font=('Helvetica', 13, 'bold'), fg=FG_COLOR, bg=BG_COLOR)
    question_label.pack(pady=20, anchor='w')

    # Option Buttons Frame
    option_frame = tk.Frame(main_frame, bg=BG_COLOR)
    option_frame.pack(pady=20, fill='x')

    # Modern Option Buttons
    btn_a = tk.Button(option_frame, text="", command=lambda: select_option(1), 
                      font=('Helvetica', 11, 'bold'), wraplength=550, 
                      bg=BG_COLOR, fg=FG_COLOR, activebackground=BUTTON_HOVER_COLOR, 
                      activeforeground=FG_COLOR, relief=tk.FLAT, bd=1, anchor='w')
    btn_b = tk.Button(option_frame, text="", command=lambda: select_option(2), 
                      font=('Helvetica', 11, 'bold'), wraplength=550,
                      bg=BG_COLOR, fg=FG_COLOR, activebackground=BUTTON_HOVER_COLOR, 
                      activeforeground=FG_COLOR, relief=tk.FLAT, bd=1, anchor='w')

    btn_a.pack(pady=10, fill='x', ipady=10)
    btn_b.pack(pady=10, fill='x', ipady=10)

    # Navigation Buttons Frame
    nav_frame = tk.Frame(main_frame, bg=BG_COLOR)
    nav_frame.pack(pady=30, fill='x')

    btn_prev = tk.Button(nav_frame, text="« Previous", command=go_previous, 
                         font=('Helvetica', 11, 'bold'), bg='#555555', fg='white', 
                         padx=15, pady=8, borderwidth=0, relief=tk.FLAT, state=tk.DISABLED)
    btn_prev.pack(side=tk.LEFT)

    btn_next = tk.Button(nav_frame, text="Next Question »", command=go_next, 
                         font=('Helvetica', 12, 'bold'), bg=ACCENT_COLOR, fg='white', 
                         padx=20, pady=8, borderwidth=0, relief=tk.FLAT)
    btn_next.pack(side=tk.RIGHT)

    display_question(progress_bar)
    root.mainloop()

# --- Run the application ---
if __name__ == "__main__":
    create_ui()
