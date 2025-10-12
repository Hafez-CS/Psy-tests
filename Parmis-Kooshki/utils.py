def get_valid_answer(options):
    for i, opt in enumerate(options, 1):
        print(f"{i}) {opt}")
    while True:
        try:
            choice = int(input("پاسخ خود را وارد کنید (عدد گزینه): "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("گزینه نامعتبر. دوباره تلاش کنید.")
        except ValueError:
            print("لطفاً فقط عدد وارد کنید.")