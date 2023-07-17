import pandas as pd
import numpy as np
import openpyxl

# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)
# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)
# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', None)
# чтобы отображалось везде 2 знака поле запятой
pd.set_option('display.float_format', '{:.2f}'.format)


# получение данных
url_doc = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRCBJkN--wKO_cWKfD51GMQ0rONZiHd7tmExSZuq_Ldp0W4tXK9Y6Akvs19lU3ZpCj8rsk4-P2WnSlo/pub?gid=2073947349&single=true&output=csv'
data = pd.read_csv(url_doc, delimiter=',')

# удалим лишний столбец
new_data = data.drop(columns='Избранное')
# добавим нужные столбы
new_data['Дозвонов'] = [1 if x > 10 else 0 for x in new_data['Длительность звонка']]
new_data['Звонков'] = 1

# делаем сводную таблицу
table = new_data.pivot_table(index=['Исходящая линия', 'Откуда'], values=['Дозвонов', 'Звонков'],
                             aggfunc=[np.sum])
# добавляем в нее вычисляемое поле
table['Дозвоны%'] = table[('sum', 'Дозвонов')] / table[('sum', 'Звонков')]

# Функция для форматирования числа в процентный формат
def format_percent(x):
    return '{:.2%}'.format(x)
# Применяем форматирование процентного значения к столбцу '%'
table['Дозвоны%'] = table['Дозвоны%'].apply(format_percent)

print(table)

