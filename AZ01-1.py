# 1. Скачайте любой датасет с сайта https://www.kaggle.com/datasets
# Загрузите набор данных из CSV-файла в DataFrame.
# Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
# Выведите информацию о данных (.info()) и статистическое описание (.describe()).

import pandas as pd
import cv

df = pd.read_csv('World-happiness-report-updated_2024.csv')

print(df.head())
print(df.info())
print(df.describe())



