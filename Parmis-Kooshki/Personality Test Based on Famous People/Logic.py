class PersonalityLogic:
    def __init__(self, gender, answers):
        self.gender = gender
        self.answers = answers

    def analyze(self):
        
        total_score = sum(self.answers) 
        avg_score = total_score / len(self.answers)

        if self.gender == "زن":
            return self.analyze_female(avg_score)
        else:
            return self.analyze_male(avg_score)

    def analyze_male(self, score):
        
        if score >= 4:
            return "تو شخصیتی شبیه ایلان ماسک داری: خلاق، جاه‌طلب و پرانرژی!"
        elif score >= 3:
            return "تو بیشتر شبیه استیو جابز هستی: عمل‌گرا و آینده‌نگر."
        elif score >= 2:
            return "تو شباهت زیادی به باراک اوباما داری: متعادل، رهبری طبیعی و آرام."
        else:
            return "تو بیشتر شبیه مارک زاکربرگ هستی: دقیق، تحلیلی و درون‌گرا."

    def analyze_female(self, score):
       
        if score >= 4:
            return "تو شخصیتی شبیه میشل اوباما داری: باانگیزه، رهبر و الهام‌بخش."
        elif score >= 3:
            return "تو بیشتر شبیه اپرا وینفری هستی: احساساتی، کاریزماتیک و باهوش اجتماعی."
        elif score >= 2:
            return "تو بیشتر شبیه شریل سندبرگ هستی: قوی، منطقی و سازمان‌دهنده عالی."
        else:
            return "تو بیشتر شبیه ملاله یوسف‌زی هستی: باایمان، آرمان‌گرا و انسان‌دوست."