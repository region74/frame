from typing import Union
import pandas as pd
import numpy as np
import openpyxl
from preparData import prep_data

# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)
# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)
# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', None)
# чтобы отображалось везде 2 знака поле запятой
pd.set_option('display.float_format', '{:.2f}'.format)

data = prep_data()


# Функция для форматирования числа в процентный формат
def format_percent(x):
    return '{:.2%}'.format(x)


# По номера телефона
def table_number():
    # делаем сводную таблицу
    table = data.pivot_table(index=['Исходящая линия', 'Откуда'], values=['Дозвон', 'Звонок'],
                             aggfunc=[np.sum])
    # добавляем в нее вычисляемое поле
    table['Дозвон%'] = table[('sum', 'Дозвон')] / table[('sum', 'Звонок')]

    # Применяем форматирование процентного значения к столбцу '%'
    table['Дозвон%'] = table['Дозвон%'].apply(format_percent)
    # Возвращаем таблицу без многоуровневых индексов для удобства использования в шаблоне
    # table=table.droplevel(axis=1, level=1).reset_index()
    return table


# По номерам опенерам
def table_opener():
    table = data.pivot_table(index=['Откуда', 'Исходящая линия'], values=['Звонок', 'Дозвон'],
                             aggfunc=[np.sum])
    # добавляем в нее вычисляемое поле
    table['Дозвон%'] = table[('sum', 'Дозвон')] / table[('sum', 'Звонок')]
    return table


# По времени дня
def table_time_day():
    # Делаем объект в Datatime
    data['Время'] = pd.to_datetime(data['Время'], format='%d.%m.%Y %H:%M:%S')
    # Создаем часы
    data['Часы'] = data['Время'].dt.hour
    # Делаем сводную таблицу
    table = data.pivot_table(index='Часы', values=['Звонок', 'Дозвон'], aggfunc=[np.sum])
    table['Дозвон%'] = table[('sum', 'Дозвон')] / table[('sum', 'Звонок')]
    table = table.drop(columns=('sum', 'Дозвон'))
    return table


# Опенер-телефон
def table_opener_number(options: Union[int, str]):
    table = data.pivot_table(index=['Откуда', 'Исходящая линия'], values=['Звонок', 'Дозвон'],
                             aggfunc=[np.sum], fill_value=0)
    # разрез звонков
    if options == 1:
        # Убираю лишнее поле
        table = table.drop(columns=('sum', 'Дозвон'))
        table2 = table.pivot_table(index='Откуда', columns='Исходящая линия', fill_value=0)
        return table2

    # разрез дозвонов
    elif options == 2:
        # добавляем в нее вычисляемое поле
        table['Дозвон%'] = table[('sum', 'Дозвон')] / table[('sum', 'Звонок')]
        table = table.drop(columns=('sum', 'Дозвон'))
        table = table.drop(columns=('sum', 'Звонок'))
        # сводная от сводной, чтобы имея проценты разбить по номерам в столбцах
        table2 = table.pivot_table(index='Откуда', columns='Исходящая линия', fill_value=0)
        return table2

    # Аналог создания первой сводной, только иными инструментами
    # table = data.groupby(['Откуда', 'Исходящая линия']).agg({'Звонок': np.sum, 'Дозвон': np.sum})
    # table['%дозвон']=table['Дозвон'] / table['Звонок']


# Опенер-время
def table_opener_time(options: Union[int, str]):
    # Делаем объект в Datatime
    data['Время'] = pd.to_datetime(data['Время'], format='%d.%m.%Y %H:%M:%S')
    # Создаем часы
    data['Часы'] = data['Время'].dt.hour
    table = data.pivot_table(index=['Откуда', 'Часы'], values=['Звонок', 'Дозвон'],
                             aggfunc=[np.sum], fill_value=0)
    # разрез звонков
    if options == 1:
        # Убираю лишнее поле
        table = table.drop(columns=('sum', 'Дозвон'))
        table2 = table.pivot_table(index='Откуда', columns='Часы', fill_value=0)
        return table2
    # разрез дозвонов
    elif options == 2:
        # добавляем в нее вычисляемое поле
        table['Дозвон%'] = table[('sum', 'Дозвон')] / table[('sum', 'Звонок')]
        table = table.drop(columns=('sum', 'Дозвон'))
        table = table.drop(columns=('sum', 'Звонок'))
        # сводная от сводной, чтобы имея проценты разбить по номерам в столбцах
        table2 = table.pivot_table(index='Откуда', columns='Часы', fill_value=0)
        return table2
