import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("آزمون اظطراب امحان")
root.geometry("720x780")
root.configure(bg="#f6f3ff")

questions = [
    " قبل از امتحان احساس دل‌درد یا تپش قلب دارم",
    " موقع امتحان ذهنم خالی می‌شود و تمرکز ندارم",
    " از فکر کردن به امتحان آینده نگران می‌شوم",
    " قبل از امتحان نمی‌توانم خوب بخوابم",
    " هنگام امتحان احساس ترس یا اضطراب دارم",
    " نگران هستم نمره بدی بگیرم حتی اگر آماده باشم",
    " وقتی دیگران راحت امتحان می‌دهند، من استرس می‌گیرم",
    " موقع امتحان دستانم می‌لرزد یا عرق می‌کنم",
    " گاهی از ترس امتحان بهانه می‌آورم تا درس نخوانم",
    " بعد از امتحان هم مدام به اشتباهاتم فکر می‌کنم"
]

choices = ["هرگز", "گاهی", "اغلب", "همیشه"]
selected_vars = [tk.IntVar(value=0) for _ in questions]

# ---------------- صفحه اول ----------------
frame_page1 = tk.Frame(root, bg="#f6f3ff")
frame_page1.pack(fill="both", expand=True)

title_label = tk.Label(frame_page1, text="آزمون اظطراب امتحان",
                       font=("IRANSans", 20, "bold"), bg="#f6f3ff", fg="#6c3bf5", pady=20)
title_label.pack()

desc_label = tk.Label(frame_page1, text="به هر سؤال صادقانه پاسخ دهید",
                      font=("IRANSans", 13), bg="#f6f3ff", fg="#444")
desc_label.pack(pady=10)

for i in range(5):
    q_frame = tk.Frame(frame_page1, bg="#ffffff", bd=2, relief="ridge")
    q_frame.pack(padx=20, pady=8, fill="x")

    tk.Label(q_frame, text=questions[i], bg="#ffffff", anchor="w", justify="right",
             font=("IRANSans", 12)).pack(padx=10, pady=5, anchor="e")

    options_frame = tk.Frame(q_frame, bg="#ffffff")
    options_frame.pack(anchor="e", pady=5)

    for j, c in enumerate(choices, start=1):
        tk.Radiobutton(options_frame, text=c, variable=selected_vars[i], value=j,
                       font=("IRANSans", 11), bg="#ffffff", fg="#333",
                       selectcolor="#f0e9ff", activebackground="#f0e9ff").pack(side="right", padx=10)


def go_to_page2():
    for i in range(5):
        if selected_vars[i].get() == 0:
            messagebox.showwarning("اخطار", "لطفاً به تمام سؤالات این بخش پاسخ دهید ")
            return
    frame_page1.pack_forget()
    frame_page2.pack(fill="both", expand=True)


next_btn = tk.Button(frame_page1, text="ادامه ➡", font=("IRANSans", 14, "bold"),
                     bg="#ff7b00", fg="white", activebackground="#e06b00",
                     relief="flat", padx=25, pady=10, command=go_to_page2)
next_btn.pack(pady=20)


# ---------------- صفحه دوم ----------------
frame_page2 = tk.Frame(root, bg="#f6f3ff")

title_label2 = tk.Label(frame_page2, text="آزمون اظطراب امتحان",
                        font=("IRANSans", 20, "bold"), bg="#f6f3ff", fg="#6c3bf5", pady=20)
title_label2.pack()

for i in range(5, 10):
    q_frame = tk.Frame(frame_page2, bg="#ffffff", bd=2, relief="ridge")
    q_frame.pack(padx=20, pady=8, fill="x")

    tk.Label(q_frame, text=questions[i], bg="#ffffff", anchor="w", justify="right",
             font=("IRANSans", 12)).pack(padx=10, pady=5, anchor="e")

    options_frame = tk.Frame(q_frame, bg="#ffffff")
    options_frame.pack(anchor="e", pady=5)

    for j, c in enumerate(choices, start=1):
        tk.Radiobutton(options_frame, text=c, variable=selected_vars[i], value=j,
                       font=("IRANSans", 11), bg="#ffffff", fg="#333",
                       selectcolor="#f0e9ff", activebackground="#f0e9ff").pack(side="right", padx=10)


def show_result():
    for v in selected_vars:
        if v.get() == 0:
            messagebox.showwarning("اخطار", "لطفاً به تمام سؤالات پاسخ دهید ")
            return

    total = sum(v.get() for v in selected_vars)
    score = int((total / (len(selected_vars) * 4)) * 100)

    frame_page2.pack_forget()
    frame_result.pack(fill="both", expand=True)

    result_label.config(text=f"اضطراب شما: {score} از ۱۰۰")

    if score <= 40:
        level = "✅ اضطراب شما پایین است.\nدر کنترل هیجانات خود مهارت دارید"
    elif score <= 70:
        level = "⚖ اضطراب شما متوسط است.\nکمی استرس طبیعی است، اما با تمرین آرام‌سازی بهتر می‌شود"
    else:
        level = "⚠ اضطراب شما بالاست.\nپیشنهاد می‌شود از تنفس عمیق و تکنیک‌های آرام‌سازی استفاده کنید"

    advice_label.config(text=level)


submit_btn = tk.Button(frame_page2, text="مشاهده نتيجه", font=("IRANSans", 14, "bold"),
                       bg="#ff7b00", fg="white", activebackground="#e06b00",
                       relief="flat", padx=25, pady=10, command=show_result)
submit_btn.pack(pady=20)


# ---------------- صفحه نتیجه ----------------
frame_result = tk.Frame(root, bg="#fff8f1")

result_label = tk.Label(frame_result, text="", font=("IRANSans", 22, "bold"),
                        fg="#ff7b00", bg="#fff8f1", pady=30)
result_label.pack()

advice_label = tk.Label(frame_result, text="", font=("IRANSans", 14),
                        fg="#333", bg="#fff8f1", wraplength=600, justify="center")
advice_label.pack(pady=10)


def restart():
    for v in selected_vars:
        v.set(0)
    frame_result.pack_forget()
    frame_page1.pack(fill="both", expand=True)


retry_btn = tk.Button(frame_result, text="تلاش دوباره",
                      font=("IRANSans", 13, "bold"), bg="#6c3bf5", fg="white",
                      activebackground="#532cd0", relief="flat", padx=20, pady=8,
                      command=restart)
retry_btn.pack(pady=20)

root.mainloop()
