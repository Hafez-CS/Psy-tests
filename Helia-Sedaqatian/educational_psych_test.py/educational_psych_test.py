# filename: educational_psych_test.py
# آزمون روانشناسی در دسته "تحصیلی" - رابط کاربری ساده با tkinter
# توضیحات:
# - این برنامه یک پرسشنامه‌ی تحصیلی با مقیاس لیکرت 5 درجه‌ای نمایش می‌دهد.
# - پاسخ‌ها ذخیره شده و در پایان نمره کلی و تفسیر نمایش داده می‌شود.
# - خروجی در فایل CSV ذخیره می‌شود (نام فایل: results.csv).
# اجرا: python educational_psych_test.py

import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

# ==== تنظیمات پرسشنامه ====
QUESTIONS = [
    "من معمولاً برای درس‌ها برنامه‌ریزی مشخصی دارم.",
    "وقتی برای امتحان آماده می‌شوم، به راحتی حواس‌پرتی پیدا نمی‌کنم.",
    "آموزش و یادگیری برای من اهمیت زیادی دارد.",
    "من می‌توانم خودم را برای مطالعهٔ سخت و طولانی‌مدت انگیزه‌دار نگه دارم.",
    "در زمان امتحان اضطراب شدیدی ندارم.",
    "من از تکنیک‌های مطالعه (خلاصه‌نویسی، فلش‌کارت و ...) استفاده می‌کنم.",
    "هنگام یادگیری مطالب جدید سریع ارتباط بین مفاهیم را می‌فهمم.",
    "من به بازخورد معلم یا اساتیدم توجه می‌کنم و آن را به کار می‌گیرم.",
    "محیط مطالعهٔ من معمولاً آرام و مناسب است.",
    "من اهداف تحصیلی مشخص و قابل اندازه‌گیری تعیین می‌کنم."
]

# مقیاس لیکرت 5 درجه‌ای: 5=کاملاً موافق ... 1=کاملاً مخالف
OPTIONS = [
    (5, "کاملاً موافق"),
    (4, "موافق"),
    (3, "نه موافق نه مخالف"),
    (2, "مخالف"),
    (1, "کاملاً مخالف")
]

# تفسیر نمره کلی (نمونه - قابل ویرایش)
def interpret_score(score, max_score):
    pct = score / max_score
    if pct >= 0.85:
        return "بسیار توانمند در مولفه‌های تحصیلی — استراتژی‌ها و انگیزهٔ قوی دارید."
    elif pct >= 0.7:
        return "خوب — مهارت‌ها و انگیزهٔ مناسبی دارید اما جا برای بهتر شدن وجود دارد."
    elif pct >= 0.5:
        return "متوسط — برخی نقاط قوت دارید اما باید روی برنامه‌ریزی و تکنیک‌ها کار کنید."
    else:
        return "پایین — پیشنهاد می‌شود برنامهٔ مطالعه، مدیریت زمان و تکنیک‌های یادگیری را بهبود دهید."

# ذخیرهٔ نتایج در CSV
def save_results(user_name, answers, score, max_score):
    filename = 'results.csv'
    header = ['timestamp', 'name'] + [f'q{i+1}' for i in range(len(QUESTIONS))] + ['score', 'max_score']
    row = [datetime.now().isoformat(), user_name] + answers + [score, max_score]
    try:
        # بررسی وجود فایل و نوشتن هدر در صورت لزوم
        write_header = False
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as f:
                pass
        except FileNotFoundError:
            write_header = True

        with open(filename, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if write_header:
                writer.writerow(header)
            writer.writerow(row)
        return True
    except Exception as e:
        print('Error saving:', e)
        return False

# ==== رابط کاربری با tkinter ====
class PsychTestApp:
    def __init__(self, master):
        self.master = master
        master.title('آزمون روانشناسی - دسته تحصیلی')
        master.geometry('700x420')

        self.user_name = tk.StringVar()
        self.current_q = 0
        self.answers = [None] * len(QUESTIONS)

        # فریم بالایی: نام آزمون‌دهنده
        top_frame = tk.Frame(master, pady=8)
        top_frame.pack(fill='x')
        tk.Label(top_frame, text='نام شما:', font=('Helvetica', 11)).pack(side='left', padx=(10,5))
        tk.Entry(top_frame, textvariable=self.user_name, width=30).pack(side='left')

        # فریم سؤال
        self.q_frame = tk.Frame(master, padx=12, pady=10)
        self.q_frame.pack(fill='both', expand=True)

        self.q_label = tk.Label(self.q_frame, text='', wraplength=640, justify='right', font=('Helvetica', 14))
        self.q_label.pack(pady=(10,20))

        # انتخابگر پاسخ
        self.choice_var = tk.IntVar()
        self.option_buttons = []
        for val, text in OPTIONS:
            rb = tk.Radiobutton(self.q_frame, text=text, variable=self.choice_var, value=val, anchor='e', justify='right', font=('Helvetica', 12))
            rb.pack(fill='x', padx=20, pady=3)
            self.option_buttons.append(rb)

        # فریم کنترل‌ها
        ctrl_frame = tk.Frame(master, pady=8)
        ctrl_frame.pack(fill='x')

        self.back_btn = tk.Button(ctrl_frame, text='قبلی', command=self.go_back, width=10)
        self.back_btn.pack(side='left', padx=10)

        self.next_btn = tk.Button(ctrl_frame, text='بعدی', command=self.go_next, width=10)
        self.next_btn.pack(side='left')

        self.finish_btn = tk.Button(ctrl_frame, text='پایان و ثبت', command=self.finish, width=14)
        self.finish_btn.pack(side='right', padx=10)

        self.progress_label = tk.Label(ctrl_frame, text='سوال 0 از 0')
        self.progress_label.pack(side='right', padx=10)

        self.update_question()

    def update_question(self):
        q_text = QUESTIONS[self.current_q]
        self.q_label.config(text=f'{self.current_q+1}. {q_text}')
        # تنظیم مقدار رادیوباکس بر اساس پاسخ موجود
        ans = self.answers[self.current_q]
        if ans is None:
            self.choice_var.set(0)
        else:
            self.choice_var.set(ans)
        self.progress_label.config(text=f'سوال {self.current_q+1} از {len(QUESTIONS)}')
        # غیرفعال/فعال کردن دکمهٔ قبلی
        if self.current_q == 0:
            self.back_btn.config(state='disabled')
        else:
            self.back_btn.config(state='normal')

    def go_next(self):
        val = self.choice_var.get()
        if val == 0:
            if not messagebox.askyesno('پرسش بدون پاسخ', 'شما به این سوال پاسخی انتخاب نکرده‌اید. می‌خواهید بدون پاسخ ادامه دهید؟'):
                return
        else:
            self.answers[self.current_q] = val
        if self.current_q < len(QUESTIONS) - 1:
            self.current_q += 1
            self.update_question()
        else:
            messagebox.showinfo('پایان سوالات', 'شما به آخرین سوال رسیدید. برای ثبت، دکمه "پایان و ثبت" را بزنید.')

    def go_back(self):
        # ذخیرهٔ پاسخ فعلی
        val = self.choice_var.get()
        if val != 0:
            self.answers[self.current_q] = val
        if self.current_q > 0:
            self.current_q -= 1
            self.update_question()

    def finish(self):
        # ذخیرهٔ پاسخ فعلی
        val = self.choice_var.get()
        if val != 0:
            self.answers[self.current_q] = val

        # بررسی هر سوالی که بدون پاسخ مانده را با مقدار 0 در نظر می‌گیریم
        answered = [a if a is not None else 0 for a in self.answers]
        # اگر کاربر هیچ پاسخی نداده باشد، هشداری نشان دهیم
        if all(a == 0 for a in answered):
            messagebox.showwarning('بدون پاسخ', 'شما هیچ پاسخی ثبت نکرده‌اید.')
            return

        score = sum(answered)
        max_score = len(QUESTIONS) * 5
        interp = interpret_score(score, max_score)

        # نمایش نتیجه
        res_text = f"نمرهٔ شما: {score} از {max_score}\n\nتفسیر: {interp}"
        messagebox.showinfo('نتیجهٔ آزمون', res_text)

        # ذخیره در فایل
        name = self.user_name.get().strip()
        if name == '':
            if not messagebox.askyesno('نام وارد نشده', 'نام وارد نشده است. آیا مایلید بدون نام ذخیره شود؟'):
                return
        saved = save_results(name, answered, score, max_score)
        if saved:
            messagebox.showinfo('ذخیره شد', 'نتیجه شما در فایل results.csv ذخیره شد.')
        else:
            messagebox.showerror('خطا', 'خطا در ذخیرهٔ نتیجه. لطفاً دسترسی فایل را بررسی کنید.')

        # بستن برنامه پس از ثبت
        self.master.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = PsychTestApp(root)
    root.mainloop()
