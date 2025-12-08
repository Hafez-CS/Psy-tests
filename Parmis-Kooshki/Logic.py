from utils import get_valid_answer
from questions import questions


class MBTIScorer:
    """مدیریت محاسبه‌ی امتیازها برای ابعاد شخصیتی MBTI"""

    def __init__(self):
        self.scores = {
            "E": 0, "I": 0,
            "S": 0, "N": 0,
            "T": 0, "F": 0,
            "J": 0, "P": 0
        }

    def update_score(self, answer, dimension):
        """به‌روزرسانی امتیاز بر اساس پاسخ و بُعد شخصیتی"""
        if dimension == "E/I":
            if answer == 1:
                self.scores["E"] += 1
            elif answer == 3:
                self.scores["I"] += 1
        elif dimension == "S/N":
            if answer == 1:
                self.scores["S"] += 1
            elif answer == 3:
                self.scores["N"] += 1
        elif dimension == "T/F":
            if answer == 1:
                self.scores["T"] += 1
            elif answer == 3:
                self.scores["F"] += 1
        elif dimension == "J/P":
            if answer == 1:
                self.scores["J"] += 1
            elif answer == 3:
                self.scores["P"] += 1

    def calculate(self, answers, questions):
        """محاسبه‌ی نهایی امتیازها"""
        for ans, q in zip(answers, questions):
            self.update_score(ans, q["dimension"])
        return self.scores

    def determine_personality(self):
        """تشخیص تیپ شخصیتی نهایی"""
        return (
            ("E" if self.scores["E"] >= self.scores["I"] else "I") +
            ("S" if self.scores["S"] >= self.scores["N"] else "N") +
            ("T" if self.scores["T"] >= self.scores["F"] else "F") +
            ("J" if self.scores["J"] >= self.scores["P"] else "P")
        )


class MBTITest:
    """کلاس اصلی برای اجرای تست MBTI"""

    def __init__(self, questions):
        self.questions = questions
        self.answers = []
        self.scorer = MBTIScorer()

    def ask_question(self, index, question):
        """پرسیدن یک سؤال از کاربر"""
        print(f"\nسؤال {index + 1}: {question['question']}")
        print("گزینه‌ها: 1) موافقم  |  2) تاحدی  |  3) مخالفم")
        return get_valid_answer(["موافقم", "تاحدی", "مخالفم"])

    def conduct_test(self):
        """اجرای کامل تست"""
        print(" تست شخصیتی MBTI آغاز شد!\n")
        for i, q in enumerate(self.questions):
            answer = self.ask_question(i, q)
            self.answers.append(answer)

        print("\n محاسبه نتایج ...")
        scores = self.scorer.calculate(self.answers, self.questions)
        personality = self.scorer.determine_personality()

        self.show_result(personality)

    def show_result(self, personality):
        """نمایش نتیجه‌ی نهایی"""
        print("\n تست شما به پایان رسید!")
        print(f" تیپ شخصیتی شما: {personality}")
        print(" ممنون که در تست MBTI شرکت کردید.")


if __name__ == "__main__":
    test = MBTITest(questions)
    test.conduct_test()
