import tkinter as tk
from tkinter import messagebox

# تعریف موقعیت‌ها و گزینه‌ها
questions = [
    {
        "question": "تو در یک گروه کاری هستی و پروژه مهمی به شما سپرده شده. یکی از اعضای گروه اشتباهی می‌کنه",
        "options": ["فکر می‌کنم اشتباه طبیعی بوده و با هم می‌تونیم جبران کنیم", 
                    "فکر می‌کنم نشانه کم‌کاری اوست و ممکنه پروژه خراب بشه"]
    },
    {
        "question": "یک دوست قدیمی تماس می‌گیره و میگه می‌خواد یک پیشنهاد غیرمنتظره بده",
        "options": ["هیجان‌زده می‌شم و انتظار یه چیز مثبت دارم",
                    "نگران می‌شم که شاید قصدش سوءاستفاده باشه"]
    },
    {
        "question": "یک پیام ناشناس در شبکه اجتماعی دریافت می‌کنی که تعریف یا انتقاد مبهمی کرده",
        "options": ["فکر می‌کنم نیت مثبت داشته و ارزشمند بوده",
                    "فکر می‌کنم قصد توهین یا ناراحتی داشته"]
    },
    {
        "question": "تو در یک صف طولانی هستی و کسی جلوتر از تو خط را می‌شکند",
        "options": ["فرض می‌کنم فوراً کارش ضروری بوده و مشکلی نیست",
                    "فرض می‌کنم آدم خودخواهیه و عصبی می‌شم"]
    },
    {
        "question": "یک فرصت شغلی یا آموزشی غیرمنتظره بهت پیشنهاد می‌شود",
        "options": ["فکر می‌کنم تجربه جدید مفید خواهد بود و ارزش ریسک داره",
                    "فکر می‌کنم احتمال شکست زیاد است و بهتره رد کنم"]
    },
    {
        "question": "یکی از همکاران یا دوستانت نظر مخالف می‌دهد",
        "options": ["فکر می‌کنم دیدگاه او مکمل من باشه و می‌تونه کمکم کنه",
                    "فکر می‌کنم قصد تخریب یا بی‌ارزش کردن من رو داره"]
    },
    {
        "question": "در یک موقعیت اجتماعی، خبری غیرمنتظره می‌شنوی که ممکنه روی برنامه‌هات تاثیر بذاره",
        "options": ["فکر می‌کنم می‌تونم از شرایط به نفع خودم استفاده کنم",
                    "فکر می‌کنم همه چیز خراب خواهد شد و کنترلش از دستم خارج است"]
    },
    {
        "question": "یک فرد غریبه بهت کمک غیرمنتظره‌ای می‌کنه",
        "options": ["فرض می‌کنم او آدم مهربون و صادقیه",
                    "فرض می‌کنم قصدی پشتش هست و چیزی می‌خواد ازم بگیره"]
    },
    {
        "question": "یک اتفاق کوچک و غیرمنتظره تو روزت رخ می‌دهد",
        "options": ["فکر می‌کنم می‌تونه تجربه یا فرصت جدید ایجاد کنه",
                    "فکر می‌کنم روزم خراب شد و هیچ چیزی درست پیش نمی‌ره"]
    },
    {
        "question": "در پایان هفته، به خودت نگاه می‌کنی و ارزیابی می‌کنی که چقدر کارهات پیش رفت",
        "options": ["تمرکز می‌کنم روی موفقیت‌ها و نکات مثبت هفته",
                    "روی شکست‌ها و مشکلات تمرکز می‌کنم و ناامید می‌شم"]
    }
]

# متغیر برای ذخیره امتیازها
score = 0
current_q = 0

# تابع ثبت پاسخ
def select_option(option):
    global score, current_q
    # اگر گزینه 0 (خوش‌بین) انتخاب شد، یک امتیاز بده
    if option == 0:
        score += 1
    current_q += 1
    if current_q < len(questions):
        update_question()
    else:
        show_result()

# تابع برای نمایش سوال بعدی
def update_question():
    q_label.config(text=questions[current_q]["question"])
    btn1.config(text=questions[current_q]["options"][0])
    btn2.config(text=questions[current_q]["options"][1])

# تابع نمایش نتیجه
def show_result():
    percentage = score / len(questions) * 100
    message = f"نتایج شما:\nخوش‌بینی: {percentage}%\nبدبینی: {100-percentage}%\n\n"
    if percentage > 60:
        message += "شما فردی خوش‌بین هستید"
    elif percentage < 40:
        message += "شما فردی بدبین هستید"
    else:
        message += "شما تعادل بین خوش‌بینی و بدبینی دارید"
    messagebox.showinfo("نتیجه تست", message)
    root.destroy()

# رابط کاربری Tkinter
root = tk.Tk()
root.title("تست خوش‌بینی و بدبینی")
root.geometry("700x300")
root.config(bg="#f0f8ff")

q_label = tk.Label(root, text="", wraplength=650, font=("Helvetica", 14), bg="#f0f8ff")
q_label.pack(pady=30)

btn1 = tk.Button(root, text="", width=60, height=2, command=lambda: select_option(0), bg="#90ee90")
btn1.pack(pady=10)

btn2 = tk.Button(root, text="", width=60, height=2, command=lambda: select_option(1), bg="#ff7f7f")
btn2.pack(pady=10)

update_question()
root.mainloop()
