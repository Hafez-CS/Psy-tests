import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk 
from operator import itemgetter
from data import QUESTIONS, FIELD_MAPPING, SUGGESTIONS # ایمپورت از data.py

class AssessmentAppTkinter:
    def __init__(self, master):
        self.master = master
        master.title("💻 ارزیابی جامع حوزه‌های برنامه‌نویسی 💻")
        master.geometry("650x450")
        master.resizable(False, False)
        
        # ۲. فعال‌سازی تم تیره Equilux
        master.set_theme("equilux") 
        
        self.master.option_add('*Font', 'Tahoma 10')
        
        self.question_keys = list(QUESTIONS.keys()) 
        self.current_q_index = 0
        self.user_scores = {q_num: tk.IntVar(value=0) for q_num in QUESTIONS}
        self.radio_buttons = []

        # --- UI Setup ---
        
        self.question_display_frame = ttk.Frame(master, padding="20")
        self.question_display_frame.pack(fill="both", expand=True)

        self.nav_frame = ttk.Frame(master, padding="10 15")
        self.nav_frame.pack(fill="x")
        
        style = ttk.Style()
        # استایل دکمه‌های ناوبری اصلی (تیره‌رنگ)
        style.configure('T.TButton', font=('Tahoma', 10, 'bold'), padding=8, foreground="white", background="#008080")
        # استایل دکمه بستن در پنجره نتایج (زرد/طلایی برای دید بهتر در Toplevel)
        style.configure('ResultClose.TButton', font=('Tahoma', 10, 'bold'), padding=8, foreground="#333333", background="#FFD700")

        
        self.prev_button = ttk.Button(self.nav_frame, text="سوال قبلی", command=self.go_prev, style='T.TButton')
        self.next_button = ttk.Button(self.nav_frame, text="سوال بعدی", command=self.go_next, style='T.TButton')
        self.result_button = ttk.Button(self.nav_frame, text=" نمایش نتایج ", command=self.show_results, style='T.TButton', state='disabled')
        
        self.progress_bar = ttk.Progressbar(self.nav_frame, orient="horizontal", length=200, mode='determinate', maximum=len(QUESTIONS))
        self.progress_label = ttk.Label(self.nav_frame, text="0/25")

        self.prev_button.pack(side="left", padx=10)
        self.result_button.pack(side="right", padx=10)
        self.next_button.pack(side="right", padx=10)
        
        self.progress_label.pack(side="top")
        self.progress_bar.pack(side="top", fill='x', padx=20)
        
        # --- فعال‌سازی میانبرهای صفحه کلید ---
        self.master.bind('<Return>', self.handle_enter) 
        self.master.bind('<Right>', lambda e: self.change_score(1)) 
        self.master.bind('<Left>', lambda e: self.change_score(-1)) 
        
        self.show_question()

    # ------------------------------------------------------------------
    # --- مدیریت میانبرهای صفحه کلید و ناوبری ---
    # ------------------------------------------------------------------
    
    def handle_enter(self, event):
        """مدیریت کلید اینتر برای رفتن به سوال بعدی یا نمایش نتایج."""
        if self.current_q_index < len(self.question_keys) - 1:
            self.go_next()
        elif self.current_q_index == len(self.question_keys) - 1 and self.user_scores[self.question_keys[self.current_q_index]].get() != 0:
            self.show_results(None)

    def change_score(self, direction):
        """تغییر نمره با کلیدهای جهت‌نما (راست/چپ)."""
        q_num = self.question_keys[self.current_q_index]
        current_score = self.user_scores[q_num].get()
        
        if current_score == 0:
            new_score = 5 if direction == -1 else 1
        else:
            new_score = current_score + direction
        
        if 1 <= new_score <= 5:
            self.user_scores[q_num].set(new_score)
            self.update_progress() 

            for rb in self.radio_buttons:
                if rb.cget('value') == str(new_score):
                    rb.focus_set()
                    break

    def clear_frame(self):
        """حذف محتوای قبلی و پاک کردن لیست رادیوباتن‌ها."""
        for widget in self.question_display_frame.winfo_children():
            widget.destroy()
        self.radio_buttons.clear()

    def update_progress(self):
        """به‌روزرسانی نوار پیشرفت و وضعیت دکمه‌ها."""
        total_questions = len(self.question_keys)
        current_q_num = self.current_q_index + 1
        
        self.progress_label.config(text=f"{current_q_num}/{total_questions}")
        self.progress_bar['value'] = current_q_num
        
        self.prev_button.config(state='normal' if self.current_q_index > 0 else 'disabled')
        
        q_num = self.question_keys[self.current_q_index]
        is_answered = self.user_scores[q_num].get() != 0

        if current_q_num < total_questions:
            self.next_button.config(state='normal')
            self.result_button.config(state='disabled')
        else:
            self.next_button.config(state='disabled')
            self.result_button.config(state='normal' if is_answered else 'disabled')
            
    def show_question(self):
        """نمایش سوال جاری."""
        self.clear_frame()
        q_num = self.question_keys[self.current_q_index]
        question_text = QUESTIONS[q_num]
        
        ttk.Label(self.question_display_frame, 
                  text=question_text, 
                  wraplength=600, justify='right', 
                  font=("Tahoma", 14, "bold"),
                  foreground="#00BFFF").pack(anchor="e", pady=(20, 30))
        
        score_frame = ttk.Frame(self.question_display_frame)
        score_frame.pack(anchor="center", pady=20)
        
        ttk.Label(score_frame, text=":نمره", font=("Tahoma", 12, "bold")).pack(side="right", padx=15)
        
        for score in range(5, 0, -1):
            rb = ttk.Radiobutton(
                score_frame, 
                text=str(score), 
                value=score, 
                variable=self.user_scores[q_num],
                command=self.update_progress 
            )
            rb.pack(side="right", padx=10)
            self.radio_buttons.append(rb)
            
        self.update_progress()
        self.master.update_idletasks()
        
        self.question_display_frame.focus_set()


    def go_next(self):
        """رفتن به سوال بعدی."""
        q_num = self.question_keys[self.current_q_index]
        if self.user_scores[q_num].get() == 0:
            messagebox.showwarning("هشدار", "لطفاً قبل از رفتن به سوال بعدی، یک گزینه را انتخاب کنید.")
            return

        if self.current_q_index < len(self.question_keys) - 1:
            self.current_q_index += 1
            self.show_question()

    def go_prev(self):
        """رفتن به سوال قبلی."""
        if self.current_q_index > 0:
            self.current_q_index -= 1
            self.show_question()

    # ------------------------------------------------------------------
    # --- منطق محاسبات و نمایش نتایج ---
    # ------------------------------------------------------------------

    def calculate_results(self):
        """محاسبه نهایی امتیازات بر اساس پاسخ‌ها."""
        user_scores_values = {q: var.get() for q, var in self.user_scores.items()}
        
        missing_answers = sum(1 for score in user_scores_values.values() if score == 0)
        if missing_answers > 0:
            messagebox.showerror("خطا", f"❌ لطفاً به تمامی {missing_answers} سوال پاسخ دهید.")
            return None
            
        field_totals = {}
        for field, q_list in FIELD_MAPPING.items():
            total_score = sum(user_scores_values.get(q_num, 0) for q_num in q_list)
            field_totals[field] = total_score
            
        # محاسبه امتیاز ویژه برای Full-stack بر اساس نسبت FE و BE
        fe_score = field_totals.get("Front-end (FE) 🎨", 0)
        be_score = field_totals.get("Back-end (BE) ⚙️", 0)
        
        num_fe_qs = len(FIELD_MAPPING["Front-end (FE) 🎨"])
        num_be_qs = len(FIELD_MAPPING["Back-end (BE) ⚙️"])
        
        combined_score = 0
        max_fe = num_fe_qs * 5
        max_be = num_be_qs * 5
        
        if max_fe > 0 and max_be > 0:
            fe_ratio = fe_score / max_fe
            be_ratio = be_score / max_be
            combined_score = (fe_ratio * 5) + (be_ratio * 5) 
        
        field_totals["Full-stack (FS) 🔗"] += combined_score 
        
        sorted_fields = sorted(field_totals.items(), key=itemgetter(1), reverse=True)
        return sorted_fields

    def show_results(self, event=None):
        """نمایش نتایج در یک پنجره جدید (Toplevel)."""
        sorted_results = self.calculate_results()
        if not sorted_results:
            return
            
        result_window = tk.Toplevel(self.master)
        result_window.title("نتایج ارزیابی حوزه برنامه‌نویسی 🏆")
        result_window.geometry("600x650")
        result_window.transient(self.master)
        result_window.resizable(False, False)

        # تلاش برای حفظ رنگ پس‌زمینه در Toplevel
        try:
            result_window.configure(bg=self.master.cget('bg'))
        except Exception:
            pass

        result_frame = ttk.Frame(result_window, padding="15")
        result_frame.pack(fill="both", expand=True)

        ttk.Label(result_frame, text="تحلیل نهایی و پیشنهادات 🧠", font=("Tahoma", 14, "bold"), foreground="#FFD700").pack(pady=10, anchor="e")
        ttk.Separator(result_frame, orient='horizontal').pack(fill='x', pady=5)

        ttk.Label(result_frame, text="✅ حوزه‌های برتر شما:", font=("Tahoma", 12, "bold"), foreground="#00CED1").pack(pady=(10, 5), anchor="e")

        top_fields = sorted_results[:3]
        for i, (field, score) in enumerate(top_fields):
            field_name = field.split('(')[0].strip()
            detail = SUGGESTIONS[field]
            
            ttk.Label(result_frame, text=f"🔥 رتبه {i+1}. {field_name} (امتیاز: {score:.1f})", 
                      font=("Tahoma", 11, "bold"), foreground="#FFA07A").pack(pady=(10, 2), anchor="e")
            
            self.create_detail_label(result_frame, "هدف:", detail['تمرکز'])
            self.create_detail_label(result_frame, "ابزارهای کلیدی:", detail['مهارت‌ها'])
            self.create_detail_label(result_frame, "ویژگی شما:", detail['شما'])
        
        ttk.Separator(result_frame, orient='horizontal').pack(fill='x', pady=10)
        
        ttk.Label(result_frame, text="📊 جزئیات تمام نمرات:", font=("Tahoma", 12, "bold"), foreground="#ADD8E6").pack(pady=(10, 5), anchor="e")

        for field, score in sorted_results:
            rank_text = f"{field.split('(')[0].strip()}  ...................................  {score:.2f} امتیاز"
            ttk.Label(result_frame, text=rank_text, justify='right', font=("Tahoma", 10)).pack(fill='x', anchor="e")
        


    def create_detail_label(self, parent, title, text):
        """ایجاد لیبل برای نمایش جزئیات."""
        detail_frame = ttk.Frame(parent, padding="0 2")
        detail_frame.pack(fill='x', anchor="e")
        
        title_label = ttk.Label(detail_frame, text=f"• {title}", font=("Tahoma", 9, "bold"), foreground="#90EE90")
        title_label.pack(side="right", padx=(5, 0))
        
        text_label = ttk.Label(detail_frame, text=text, wraplength=450, justify='right', font=("Tahoma", 9))
        text_label.pack(side="right", anchor="e")


if __name__ == "__main__":

    root = ThemedTk() 
    app = AssessmentAppTkinter(root)
    root.mainloop()