class AnswerInput:
    """
    مدیریت ورودی پاسخ کاربر برای سوالات چندگزینه‌ای.
    - از ورودی عددی محافظت می‌کند.
    - در صورت خطا، پیام مناسب نشان می‌دهد.
    """

    def __init__(self, options):
        """
        :param options: لیستی از گزینه‌های ممکن برای نمایش به کاربر
        """
        self.options = options

    def display_options(self):
        """نمایش گزینه‌ها به‌صورت زیبا و شماره‌گذاری‌شده"""
        print("\nگزینه‌های موجود:")
        for i, opt in enumerate(self.options, start=1):
            print(f"  {i}. {opt}")

    def get_choice(self):
        """
        دریافت انتخاب معتبر از کاربر.
        در صورت ورود نامعتبر، از کاربر می‌خواهد دوباره تلاش کند.
        """
        self.display_options()

        while True:
            try:
                choice = input(" عدد گزینه‌ی مورد نظر را وارد کنید: ").strip()

                if not choice.isdigit():
                    raise ValueError("ورودی باید عدد باشد.")

                choice = int(choice)
                if 1 <= choice <= len(self.options):
                    print(f" انتخاب شما: {self.options[choice - 1]}")
                    return choice

                else:
                    print(f" لطفاً عددی بین 1 تا {len(self.options)} وارد کنید.")

            except ValueError as e:
                print(f"خطا: {e}")

            print(" دوباره تلاش کنید...\n")


# تابع سازگار با نسخه‌ی قبلی برای راحتی
def get_valid_answer(options):
    """
    نسخه‌ی سازگار با سیستم قبلی برای دریافت پاسخ کاربر،
    ولی با استفاده از کلاس جدید AnswerInput.
    """
    return AnswerInput(options).get_choice()
