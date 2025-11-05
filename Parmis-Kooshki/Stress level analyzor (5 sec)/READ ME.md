🟦 English Section

Project Title: Stress Response Analysis Test

Overview:
This project is an intelligent stress response analysis system that measures how users react under time pressure. Each user answers a set of 20 psychological questions within a limited time (5 seconds per question).
Based on the answers and reaction time, the system analyzes the stress level, predicts emotional patterns, and provides personalized recommendations such as books and movies for improving emotional regulation.

Key Features:
 • ⏱️ Time-limited responses: each question must be answered in under 5 seconds to simulate stress conditions.
 • 🧠 Emotion analysis: results are processed using AI models and NLP for better understanding of emotional response.
 • 📊 Visualization dashboard: includes detailed stress level graphs using Matplotlib and Seaborn.
 • 🤖 Machine Learning integration: supports Hugging Face pretrained models for stress/emotion classification.
 • 🗄️ SQLite database: stores user data, responses, and results securely.
 • 📚 Personalized recommendations: suggests relevant books or movies based on the user’s final stress profile.
 • 🧩 Modular OOP structure: includes separate Python classes for data processing, visualization, recommendations, and database management.

Files Structure:

stress_processor.py      → Core logic and stress scoring
stress_dashboard.py      → Visualization and BI-style analytics
stress_recommended.py    → Recommendation engine (books/movies)
stress_database.py       → SQLite database connection and storage
stress_main.py           → Main entry file (user flow and question timing)


Used Libraries:
time, sqlite3, matplotlib, seaborn, tensorflow, scikit-learn, transformers, numpy, pandas


⸻

🟥 بخش فارسی

عنوان پروژه: تست تحلیل واکنش در شرایط استرس

توضیح کلی:
این پروژه یک سیستم هوشمند برای سنجش میزان استرس و واکنش احساسی کاربران در شرایط فشار زمانی است.
کاربر باید به ۲۰ سؤال روان‌شناسی در مدت ۵ ثانیه برای هر سؤال پاسخ دهد.
پاسخ‌ها و سرعت واکنش او تحلیل شده و در نهایت سطح استرس و الگوی رفتاری‌اش مشخص می‌شود.
همچنین سیستم بر اساس نتیجه نهایی، فیلم‌ها و کتاب‌های پیشنهادی برای بهبود وضعیت احساسی ارائه می‌دهد.

ویژگی‌ها:
 • ⏱️ پاسخ‌دهی زمان‌دار: هر سؤال فقط ۵ ثانیه فرصت دارد تا استرس واقعی شبیه‌سازی شود.
 • 🧠 تحلیل احساسی پیشرفته: استفاده از مدل‌های NLP و هوش مصنوعی برای تفسیر دقیق احساسات.
 • 📊 داشبورد تحلیلی گرافیکی: نمایش نمودارها و تحلیل‌ها با استفاده از Matplotlib و Seaborn.
 • 🤖 مدل‌های از پیش آموزش‌دیده (Hugging Face): برای پیش‌بینی سطح استرس و واکنش هیجانی.
 • 🗄️ پایگاه داده SQLite: ذخیره‌سازی نتایج، اطلاعات کاربر و پاسخ‌ها در دیتابیس محلی.
 • 📚 پیشنهاد کتاب و فیلم: معرفی منابع مفید برای مدیریت بهتر احساسات.
 • 🧩 ساختار کلاس‌محور و ماژولار: کدها به‌صورت تفکیک‌شده و شیءگرا در چند فایل نوشته شده‌اند.

ساختار فایل‌ها:

stress_processor.py      → پردازش پاسخ‌ها و محاسبه سطح استرس
stress_dashboard.py      → رسم نمودارها و تحلیل داده‌ها
stress_recommended.py    → پیشنهاد کتاب و فیلم بر اساس نتیجه
stress_database.py       → مدیریت پایگاه داده SQLite
stress_main.py           → منطق اصلی و نمایش سؤالات زمان‌دار


کتابخانه‌های استفاده‌شده:
time, sqlite3, matplotlib, seaborn, tensorflow, scikit-learn, transformers, numpy, pandas.