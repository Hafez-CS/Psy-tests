from TAS_processor import TASProcessor
from Emotion_predictor import EmotionPredictor
from database_manager import DatabaseManager
from visualization_dashboard import VisualizationDashboard

def main():
    print("به تست TAS خوش آمدید!\n")
    
    # مرحله ۱: ایجاد نمونه از کلاس تست
    tas = TASProcessor()
    user_data = tas.run_test()  # شامل نام، جنسیت، پاسخ‌ها، امتیاز نهایی
    
    # مرحله ۲: پیش‌ بینی واکنش احساسی
    predictor = EmotionPredictor()
    predicted_reaction = predictor.predict_reaction(user_data["score"])
    print("\n🔹 پیش‌بینی واکنش احساسی شما:")
    print(predicted_reaction)
    
    # مرحله ۳: ذخیره داده‌ها در پایگاه داده
    db = DatabaseManager()
    db.save_result(
        name=user_data["name"],
        gender=user_data["gender"],
        score=user_data["score"],
        predicted_emotion=predicted_reaction
    )
    
    # مرحله ۴: نمایش داشبورد گرافیکی
    print("\n در حال نمایش نمودارهای تحلیلی...")
    dashboard = VisualizationDashboard()
    dashboard.plot_tas_distribution()
    dashboard.plot_gender_comparison()
    dashboard.plot_emotion_vs_tas()

if name == "__main__":
    main()