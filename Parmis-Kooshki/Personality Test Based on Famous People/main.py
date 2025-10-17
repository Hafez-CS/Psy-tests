from questions import QuestionSet
from Logic import PersonalityLogic

def main():
    print(" به تست شخصیت‌شناسی خوش آمدید!")
    print("در پایان تست، به شما گفته می‌شود شبیه کدام شخصیت معروف هستید.\n")

   
    gender = input("لطفاً جنسیت خود را وارد کنید (زن / مرد): ").strip()

    while gender not in ["زن", "مرد"]:
        gender = input("لطفاً فقط 'زن' یا 'مرد' را وارد کنید: ").strip()


    qs = QuestionSet(gender)

    print("\nپاسخ‌هایت را وارد کن:\n(1=کاملاً مخالفم, 2=مخالفم, 3=متوسط, 4=موافقم, 5=کاملاً موافقم)\n")

    answers = []
    for i, q in enumerate(qs.questions, start=1):
        while True:
            try:
                answer = int(input(f"{i}. {q}\nپاسخ شما (1 تا 5): "))
                if 1 <= answer <= 5:
                    answers.append(answer)
                    break
                else:
                    print(" لطفاً عددی بین 1 تا 5 وارد کنید.")
            except ValueError:
                print(" ورودی نامعتبر است. فقط عدد وارد کنید.")

   
    logic = PersonalityLogic(gender, answers)
    result = logic.analyze()


    print("\n نتیجه تست شما:")
    print(result)
    print("\nاز شرکت در تست شخصیت‌شناسی ما متشکریم ")


if __name__ == "__main__":
    main()