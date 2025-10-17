class QuestionSet:
    def __init__(self, gender):
        self.gender = gender
        self.questions = self.get_questions_based_on_gender()

    def get_questions_based_on_gender(self):
       
        if self.gender == "زن":
            return [
                "من معمولاً با احساساتم تصمیم می‌گیرم.",
                "از کارهای گروهی و کمک به دیگران لذت می‌برم.",
                "برای من ارتباطات انسانی مهم‌تر از رقابت است.",
                "در شرایط سخت، آرام و منطقی می‌مانم.",
                "دوست دارم دیگران را الهام‌بخش خودم بدانم.",
                "به جزئیات و زیبایی در کارم اهمیت زیادی می‌دهم.",
            ]
        else:  
            return [
                "من معمولاً با منطق تصمیم می‌گیرم.",
                "از رقابت و چالش لذت می‌برم.",
                "در شرایط بحرانی سریع عمل می‌کنم.",
                "هدفم همیشه رسیدن به موفقیت بزرگ است.",
                "ترجیح می‌دهم رهبر باشم تا پیرو.",
                "دوست دارم با ایده‌های جدید دنیا را تغییر دهم.",
            ]
class Question:
    def __init__(self, text, options):
        self.text = text
        self.options = options  
        
    def display(self):

        print(f"\n{self.text}")
        for i, opt in enumerate(self.options, start=1):
            print(f"{i}) {opt['text']}")

    def get_answer(self):
      
        while True:
            try:
                choice = int(input("انتخاب شما (عدد گزینه): "))
                if 1 <= choice <= len(self.options):
                    return self.options[choice - 1]["person"]
                else:
                    print("لطفاً عدد معتبر وارد کنید.")
            except ValueError:
                print("ورودی نامعتبر. فقط عدد وارد کنید.")


class QuestionBank:
    def __init__(self):
        self.questions = self.load_questions()

    def load_questions(self):
       
        return [
            Question("وقتی با چالش سخت روبه‌رو می‌شی، اولین کاری که می‌کنی چیه؟", [
                {"text": "به راه‌های خلاق و متفاوت فکر می‌کنم", "person": "ایلان ماسک"},
                {"text": "جزئیات رو تحلیل می‌کنم تا بهترین تصمیم رو بگیرم", "person": "مارک زاکربرگ"},
                {"text": "با تیمم مشورت می‌کنم تا هم‌فکری کنیم", "person": "باراک اوباما"},
                {"text": "روی زیبایی و کمال کار تمرکز می‌کنم", "person": "استیو جابز"}
            ]),
            Question("وقتی کسی ازت انتقاد می‌کنه، معمولاً چطور برخورد می‌کنی؟", [
                {"text": "به عنوان فرصت رشد نگاه می‌کنم", "person": "میشل اوباما"},
                {"text": "فکر می‌کنم دیدگاهش هم ارزش شنیدن داره", "person": "اپرا وینفری"},
                {"text": "سعی می‌کنم منطقی بررسیش کنم", "person": "شریل سندبرگ"},
                {"text": "به احساساتم گوش می‌دم و مسیر خودمو می‌رم", "person": "تیلور سویفت"}
            ]),
            Question("بزرگ‌ترین انگیزه‌ت توی زندگی چیه؟", [
                {"text": "ساختن آینده‌ای متفاوت برای دنیا", "person": "ایلان ماسک"},
                {"text": "ایجاد تأثیر مثبت در جامعه", "person": "باراک اوباما"},
                {"text": "خلق محصولاتی زیبا و ماندگار", "person": "استیو جابز"},
                {"text": "یادگیری و آموزش برای بهتر شدن دنیا", "person": "بیل گیتس"}
            ])
        ]

    def get_all(self):
        
        return self.questions