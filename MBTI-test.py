import tkinter as tk

# داده ها
questions = [
    {"text": "من از بودن در جمع انرژی می‌گیرم.", "dimension": "EI"},
    {"text": "دوست دارم قبل از تصمیم‌گیری همه جزئیات را بدانم.", "dimension": "SN"},
    {"text": "در تصمیم‌گیری بیشتر از منطق استفاده می‌کنم.", "dimension": "TF"},
    {"text": "دوست دارم برنامه‌ریزی دقیقی برای کارها داشته باشم.", "dimension": "JP"},
    {"text": "معمولاً با افراد جدید راحت ارتباط می‌گیرم.", "dimension": "EI"},
    {"text": "به الهامات درونی‌ام بیشتر از واقعیت‌ها اعتماد دارم.", "dimension": "SN"},
    {"text": "احساسات دیگران برایم خیلی مهم است.", "dimension": "TF"},
    {"text": "کارها را ترجیح می‌دهم خودجوش انجام دهم تا برنامه‌ریزی‌شده.", "dimension": "JP"},
    {"text": "در جمع‌ها معمولاً فعال و پرانرژی‌ام.", "dimension": "EI"},
    {"text": "به جزئیات و واقعیت‌ها توجه زیادی دارم.", "dimension": "SN"},
    {"text": "در برخورد با مشکلات، منطقی‌تر عمل می‌کنم تا احساسی.", "dimension": "TF"},
    {"text": "دوست دارم تصمیمات را در لحظه بگیرم.", "dimension": "JP"},
]

# امتياز ها
scores = {"E":0, "I":0, "S":0, "N":0, "T":0, "F":0, "J":0, "P":0}

# توضيحات تيپ ها
descriptions = {
    "INTJ": "برنامه‌ریز، تحلیلی و آینده‌نگر",
    "INTP": "تحلیل‌گر و عاشق یادگیری مفاهیم جدید",
    "ENTJ": "باهدف، قاطع و رهبر ذاتی",
    "ENTP": "خلاق، پرانرژی و ماجراجو",
    "INFJ": "عمیق، الهام‌بخش و آرمان‌گرا",
    "INFP": "احساسی، خلاق و ایده‌آل‌گرا",
    "ENFJ": "مهربان، اجتماعی و الهام‌بخش",
    "ENFP": "پرشور، اجتماعی و دنبال آزادی",
    "ISTJ": "مسئول، دقیق و منظم",
    "ISFJ": "وفادار، دلسوز و فداکار",
    "ESTJ": "قاطع، منظم و عمل‌گرا",
    "ESFJ": "مهربان، اجتماعی و وظیفه‌شناس",
    "ISTP": "تحلیل‌گر و اهل ماجراجویی",
    "ISFP": "آرام، خلاق و عاشق زیبایی",
    "ESTP": "پرانرژی، ریسک‌پذیر و عاشق هیجان",
    "ESFP": "شاد، اجتماعی و سرگرم‌کننده"
}

# ---------------------------
# رابط کاربري
# ---------------------------
index = 0  # شماره سؤال فعلی

root = tk.Tk()
root.title("تست شخصیت MBTI 🌿")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="#f0f7f4")

question_label = tk.Label(root, text="", font=("B Nazanin", 14), bg="#f0f7f4", wraplength=400, justify="center")
question_label.pack(pady=40)

def show_question():
    if index < len(questions):
        question_label.config(text=f"سؤال {index+1}: {questions[index]['text']}")
    else:
        show_result()

def record_answer(answer):
    global index
    if index < len(questions):
        dim = questions[index]["dimension"]
        if answer == "yes":
            if dim == "EI": scores["E"] += 1
            elif dim == "SN": scores["S"] += 1
            elif dim == "TF": scores["T"] += 1
            elif dim == "JP": scores["J"] += 1
        else:
            if dim == "EI": scores["I"] += 1
            elif dim == "SN": scores["N"] += 1
            elif dim == "TF": scores["F"] += 1
            elif dim == "JP": scores["P"] += 1
        index += 1
        show_question()

def show_result():
    # محاسبه تیپ
    result = (
        ("E" if scores["E"] >= scores["I"] else "I") +
        ("S" if scores["S"] >= scores["N"] else "N") +
        ("T" if scores["T"] >= scores["F"] else "F") +
        ("J" if scores["J"] >= scores["P"] else "P")
    )

    desc = descriptions.get(result, "توضیحی در دسترس نیست.")

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="🎯 نتیجه تست شما:", font=("B Nazanin", 14), bg="#f0f7f4").pack(pady=10)
    tk.Label(root, text=result, font=("B Nazanin", 28, "bold"), bg="#f0f7f4", fg="#3a7f62").pack()
    tk.Label(root, text=desc, font=("B Nazanin", 13), wraplength=400, bg="#f0f7f4", justify="center").pack(pady=20)

# دکمه‌ها
button_frame = tk.Frame(root, bg="#f0f7f4")
button_frame.pack()

yes_button = tk.Button(button_frame, text="بله ✅", width=12, font=("B Nazanin", 12), bg="#b6e2d3", command=lambda: record_answer("yes"))
yes_button.grid(row=0, column=0, padx=20, pady=10)

no_button = tk.Button(button_frame, text="خیر ❌", width=12, font=("B Nazanin", 12), bg="#ffb3b3", command=lambda: record_answer("no"))
no_button.grid(row=0, column=1, padx=20, pady=10)

show_question()
root.mainloop()
