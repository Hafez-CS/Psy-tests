 تست شخصیت‌شناسی بر اساس شخصیت‌های معروف

## توضیح کلی
این پروژه یک تست شخصیت‌شناسی ساده است که بر اساس پاسخ‌های کاربر به چند سؤال روان‌شناسی، شباهت او را با شخصیت‌های موفق و شناخته‌شده دنیا (مانند ایلان ماسک، استیو جابز، میشل اوباما و دیگران) تحلیل می‌کند.  
کاربر در ابتدای تست، جنسیت خود را وارد می‌کند و سپس به مجموعه‌ای از سؤال‌ها پاسخ می‌دهد.  
در پایان، برنامه با استفاده از منطق از پیش‌تعریف‌شده، شخصیت کاربر را با یکی از چهره‌های معروف تطبیق می‌دهد.

## ساختار فایل‌ها
```
project/
│
├── main.py        → فایل اصلی برای اجرای برنامه
├── logic.py       → شامل منطق تحلیل و تعیین شخصیت
└── questions.py   → شامل سؤالات مخصوص هر جنسیت
```

## نحوه اجرا
1. اطمینان حاصل کنید که Python 3 روی سیستم شما نصب است.  
2. پوشه‌ی پروژه را در VS Code یا ترمینال باز کنید.  
3. دستور زیر را برای اجرای برنامه وارد کنید:
   ```
   python main.py
   ```
4. دستورالعمل‌های نمایش‌داده‌شده را دنبال کنید:
   - ابتدا جنسیت خود را وارد کنید (زن یا مرد)
   - سپس به سؤال‌ها با عددی بین 1 تا 5 پاسخ دهید
5. در پایان، نتیجه‌ی تحلیل شخصیت شما نمایش داده می‌شود.

## وابستگی‌ها
این پروژه فقط از کتابخانه‌های پیش‌فرض Python استفاده می‌کند و به نصب کتابخانه‌ی اضافی نیاز ندارد.

## هدف پروژه
هدف از این پروژه، طراحی یک تست شخصیت‌شناسی آموزشی با ساختار کلاسی و ماژولار است که بتواند به عنوان تمرین برنامه‌نویسی روان‌شناسی مورد استفاده قرار گیرد.

---

# Personality Test Based on Famous People

## Overview
This project is a simple personality test that analyzes the user's similarity to successful and well-known figures (such as Elon Musk, Steve Jobs, Michelle Obama, and others) based on their answers to a set of psychology-inspired questions.  
At the beginning of the test, the user selects their gender and then responds to several questions.  
Finally, the program evaluates the answers and determines which famous personality the user most resembles.

## File Structure
```
project/
│
├── main.py        → Main file to run the program
├── logic.py       → Contains the personality analysis logic
└── questions.py   → Contains gender-based question sets
```

## How to Run
1. Make sure Python 3 is installed on your system.  
2. Open the project folder in VS Code or any terminal.  
3. Run the program using:
   ```
   python main.py
   ```
4. Follow the on-screen instructions:
   - Enter your gender (male or female)
   - Answer each question with a number from 1 to 5
5. The program will display your personality result at the end.

## Dependencies
This project uses only Python’s built-in libraries. No external packages are required.

## Project Goal
The main goal is to design an educational, class-based, modular personality test that can be used for programming practice in psychology-related applications.