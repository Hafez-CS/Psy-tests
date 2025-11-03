import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf

class TASProcessor:
    def __init__(self):
        self.questions = [
            "۱. اغلب نمی‌دانم دقیقاً چه احساسی دارم.",
            "۲. هنگام اضطراب نمی‌دانم که مضطربم یا ناراحتم.",
            "۳. احساساتم را به سختی توصیف می‌کنم.",
            "۴. ترجیح می‌دهم درباره مشکلاتم فکر کنم تا احساساتم.",
            "۵. وقتی در جمع هستم، تشخیص احساسم برایم دشوار است.",
            "۶. نمی‌دانم درونم چه می‌گذرد.",
            "۷. وقتی احساس بدی دارم، نمی‌دانم علتش چیست.",
            "۸. ترجیح می‌دهم درباره واقعیت‌ها حرف بزنم تا احساسات.",
            "۹. در موقعیت‌های عاطفی اغلب گیج می‌شوم.",
            "۱۰. نمی‌توانم احساساتم را با کلمات بیان کنم.",
            "۱۱. نمی‌دانم چرا ناراحت یا خوشحال می‌شوم.",
            "۱۲. احساسات مردم دیگر را راحت تشخیص می‌دهم. (معکوس)",
            "۱۳. وقتی کسی ناراحت است، به راحتی درکش می‌کنم. (معکوس)",
            "۱۴. وقتی ناراحتم، می‌توانم توضیح دهم چرا. (معکوس)",
            "۱۵. از درک معنای رویاهایم عاجزم.",
            "۱۶. وقتی احساس خشم دارم، سخت شناسایی‌اش می‌کنم.",
            "۱۷. ترجیح می‌دهم منطقی فکر کنم تا احساسی.",
            "۱۸. احساساتم مبهم یا آشفته هستند.",
            "۱۹. نمی‌توانم فرق بین احساسات مشابه را بفهمم.",
            "۲۰. گاهی حس می‌کنم درونم بی‌احساس است."
        ]

        
        self.reverse_questions = [12, 13, 14]

       
        self.scaler = MinMaxScaler()
        self.regressor = LinearRegression()
        self.model = self._build_keras_model()

    def _build_keras_model(self):
        model = Sequential([
            Dense(32, input_dim=20, activation='relu'),
            Dense(16, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def calculate_score(self, answers):
        scores = []
        for i, ans in enumerate(answers, start=1):
            if i in self.reverse_questions:
                scores.append(6 - ans) 
            else:
                scores.append(ans)
        total = sum(scores)
        return total

    def interpret_score(self, total_score):
        if total_score < 51:
            return "بدون مشکل در شناسایی احساسات"
        elif 52 <= total_score <= 60:
            return "محدوده مرزی (ممکن است درک احساسات کمی دشوار باشد)"
        else:
            return "احتمال وجود الکسی‌تایمیا بالا (مشکل در شناخت یا بیان احساسات)"

    def train_mock_model(self):
        X = np.random.randint(1, 6, (200, 20))
        y = (X.mean(axis=1) > 3.2).astype(int)

        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y, epochs=5, verbose=0)

    def predict_tendency(self, answers):
        scaled = self.scaler.transform([answers])
        prediction = self.model.predict(scaled, verbose=0)
        return float(prediction[0][0])