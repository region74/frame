import pandas as pd
import numpy as np
import openpyxl

# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', None)

# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)

# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)

data_set = pd.read_excel('data.xlsx')

# добавление колонки с расчетами по формуле
data_set['dozvonli'] = [1 if x >= 30 else 0 for x in data_set['Длительность звонка']]
data_set['zvonok'] = 1
# print(data_set)
# сводная таблица
count_dozvon = data_set.pivot_table(index=['Исходящая линия', 'Откуда'], values=['dozvonli', 'zvonok'],
                                    aggfunc=[np.sum])
print(count_dozvon)

# print(data_set.head())
