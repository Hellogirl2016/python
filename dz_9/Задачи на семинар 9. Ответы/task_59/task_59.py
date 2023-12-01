"""
1. Проверить есть ли в файле пустые значения
2. Показать median_house_value где median_income < 2
3. Показать данные в первых 2 столбцах
4. Выбрать данные где housing_median_age < 20 и
median_house_value > 70000
"""

import pandas as pd

data = pd.read_csv('california_housing_test.csv')

# 1. Проверить есть ли в файле пустые значения
print(data.isnull().sum())

# 2. Показать median_house_value где median_income < 2
res = data[data['median_income'] < 2]['median_house_value']
print(res)

# 3. Показать данные в первых 2 столбцах
two_col = data[["longitude", "latitude"]]
print(two_col)
two_col = data.iloc[:, :2]
print(two_col)

# 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000
res = data[
    (data["housing_median_age"] < 20) & (data["median_house_value"] > 70000)]
print(res)
