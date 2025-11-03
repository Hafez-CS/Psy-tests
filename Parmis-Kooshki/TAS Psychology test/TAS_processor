import numpy as np

class TASProcessor:
    def __init__(self):
        self.questions = [
            "1. اغلب نمی‌دانم دقیقاً چه احساسی دارم.",
            "2. هنگام اضطراب نمی‌دانم که مضطربم یا ناراحتم.",
            "3. احساساتم را به سختی توصیف می‌کنم.",
            "4. ترجیح می‌دهم درباره مشکلاتم فکر کنم تا اینکه درباره احساساتم صحبت کنم.",
            "5. وقتی در جمع هستم، تشخیص اینکه چه احساسی دارم برایم دشوار است.",
            "6. نمی‌دانم درونم چه می‌گذرد.",
            "7. وقتی احساس بدی دارم، نمی‌دانم علتش چیست.",
            "8. ترجیح می‌دهم درباره واقعیت‌ها حرف بزنم تا احساسات.",
            "9. در موقعیت‌های عاطفی اغلب گیج می‌شوم.",
            "10. نمی‌توانم احساساتم را با کلمات درست بیان کنم.",
            "11. نمی‌دانم دقیقاً چرا ناراحت یا خوشحال می‌شوم.",
            "12. احساسات مردم دیگر را راحت تشخیص می‌دهم. (معکوس)",
            "13. وقتی کسی ناراحت است، به راحتی درکش می‌کنم. (معکوس)",
            "14. وقتی ناراحتم، می‌توانم برای دیگران توضیح دهم چرا. (معکوس)",
            "15. از درک معنای رویاهایم عاجزم.",
            "16. وقتی احساس خشم دارم، به سختی می‌توانم آن را شناسایی کنم.",
            "17. ترجیح می‌دهم کارهایی انجام دهم که نیاز به تفکر منطقی دارد نه احساسی.",
            "18. احساساتم معمولاً مبهم یا آشفته هستند.",
            "19. نمی‌توانم فرق بین احساسات مشابه مثل ترس و هیجان را بفهمم.",
            "20. گاهی حس می‌کنم درونم “بی‌احساس” است."
        ]

        
        self.reverse_items = [12, 13, 14]

       
        self.answers = []

    def run_test(self, answers=None):
        if answers is None:
            print("لطفاً برای هر سؤال عددی بین 1 تا 5 وارد کنید:")
            print("1=کاملاً مخالفم ... 5=کاملاً موافقم\n")
            for q in self.questions:
                while True:
                    try:
                        ans = int(input(f"{q}\nپاسخ: "))
                        if 1 <= ans <= 5:
                            self.answers.append(ans)
                            break
                        else:
                            print("عدد باید بین 1 تا 5 باشد.")
                    except ValueError:
                        print("ورودی نامعتبر است. لطفاً فقط عدد وارد کنید.")
        else:
            self.answers = answers

    def calculate_score(self):
        adjusted_scores = []
        for i, ans in enumerate(self.answers, start=1):
            if i in self.reverse_items:
                adjusted_scores.append(6 - ans) 
            else:
                adjusted_scores.append(ans)
        total_score = np.sum(adjusted_scores)
        return total_score

    def interpret_result(self, total_score):
        if total_score < 51:
            return "بدون مشکل در شناسایی احساسات"
        elif 51 <= total_score <= 60:
            return "مرزی (درک احساسات کمی دشوار است)"
        else:
            return "احتمال بالا برای ناتوانی در شناخت یا بیان احساسات"

    def process(self, answers=None):
        self.run_test(answers)
        score = self.calculate_score()
        result = self.interpret_result(score)
        return score, result