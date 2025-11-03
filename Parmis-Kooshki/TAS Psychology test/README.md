English Version
 This project is a simplified implementation of the TAS (Toronto Alexithymia Scale) test, 
integrated with emotion prediction and visual analytics.
 Users answer a series of situational questions, and based on their responses, a total 
score is calculated.
 The system then predicts the user’s emotional reaction using a pre-trained language 
model from Hugging Face and stores all results in a local SQLite database.
 Finally, a visual dashboard presents analytical insights through graphs that display 
score distribution, gender-based comparison, and the correlation between TAS scores 
and emotional reactions.
 Project Structure:
 • tas_processor.py: Handles the test flow and question processing.
 • emotion_predictor.py: Predicts emotional reactions using a pre-trained model.
 • database_manager.py: Manages data storage in SQLite.
 • visualization_dashboard.py: Generates analytical charts and visual reports.
 • main.py: Runs the full process step by step.
 To run the project:
 1. Make sure Python 3.9 or higher is installed.
 2. Install required libraries:
 pip install matplotlib pandas transformers torch
 3. Run the program:
 python main.py
 The program will ask the user’s name, gender, and test responses, then display the 
predicted emotional pattern and open the visual analytics dashboard automatically.
 

 نسخه فارسی

این پروژه یک پیاده‌سازی ساده از تست TAS (مقیاس آلکسی‌تیمیا تورنتو) است که با پیش‌بینی احساسات و داشبورد تحلیلی ترکیب شده است.
کاربر به مجموعه‌ای از سؤالات موقعیتی پاسخ می‌دهد و بر اساس پاسخ‌ها، امتیاز کلی محاسبه می‌شود.
سپس سیستم با استفاده از یک مدل از پیش‌آموزش‌دیده در سایت Hugging Face واکنش احساسی کاربر را پیش‌بینی کرده و نتایج را در پایگاه داده SQLite ذخیره می‌کند.
در پایان، یک داشبورد گرافیکی شامل نمودارهایی از توزیع نمرات، مقایسه بر اساس جنسیت و رابطه بین نمره TAS و واکنش احساسی نمایش داده می‌شود.

ساختار پروژه:
 • tas_processor.py: مدیریت روند تست و پردازش پاسخ‌ها
 • emotion_predictor.py: پیش‌بینی واکنش احساسی با مدل از پیش‌آموزش‌دیده
 • database_manager.py: ذخیره اطلاعات در پایگاه داده SQLite
 • visualization_dashboard.py: تولید نمودارها و تحلیل‌های بصری
 • main.py: اجرای گام‌به‌گام کل فرآیند

مراحل اجرا:
 1. اطمینان از نصب Python نسخه 3.9 یا بالاتر
 2. نصب کتابخانه‌های مورد نیاز:
pip install matplotlib pandas transformers torch
 3. اجرای برنامه:
python main.py

پس از اجرا، برنامه نام، جنسیت و پاسخ‌های کاربر را می‌پرسد، سپس الگوی احساسی پیش‌بینی‌شده را نمایش داده و داشبورد تحلیلی را به‌صورت خودکار باز می‌کند.
