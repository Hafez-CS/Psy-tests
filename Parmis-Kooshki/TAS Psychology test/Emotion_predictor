import json
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import sqlite3


from transformers import pipeline

class EmotionPredictor:
    def __init__(self):
        
        self.translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fa-en")

        
        self.emotion_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

    def predict_emotion(self, situation_fa):
        """
        پیش‌بینی احساس کاربر بر اساس متن فارسی
        """
        
        translated_text = self.translator(situation_fa)[0]['translation_text']

        
        prediction = self.emotion_model(translated_text)[0]
        emotion = prediction['label']
        score = prediction['score']

       
        emotion_fa = self._translate_emotion_to_farsi(emotion)

       
        result = {
            "متن فارسی": situation_fa,
            "ترجمه انگلیسی": translated_text,
            "احساس پیش‌بینی‌شده": emotion_fa,
            "درصد اطمینان": f"{score:.2f}"
        }

        return json.dumps(result, ensure_ascii=False, indent=2)

    def _translate_emotion_to_farsi(self, emotion):
        """
        ترجمه واکنش ها از انگلیسی به فارسی
        """
        mapping = {
            "joy": "شادی",
            "anger": "خشم",
            "sadness": "اندوه",
            "fear": "ترس",
            "surprise": "شگفتی",
            "disgust": "انزجار"
        }
        return mapping.get(emotion.lower(), "نامشخص")