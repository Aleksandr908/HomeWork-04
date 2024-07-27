# 2. Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv​

import pandas as pd

df = pd.read_csv('dz.csv')

salary_by_city = df.groupby('City')['Salary'].mean()

print(salary_by_city)
