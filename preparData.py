import pandas as pd
import numpy as np
import openpyxl

file_path = 'api/data.csv'


# Функция подготовки базовой таблицы для всех срезов
def prep_data():
    data = pd.read_csv(file_path, delimiter=';')
    # удалим лишние данные
    new_data = data.drop(
        columns=['Схема', 'Кто разговаривал', 'Кто ответил', 'Оценка', 'ID записи', 'Метка', 'Теги', 'ID заказа звонка',
                 'Запись существует', 'Новый клиент', 'Состояние перезвона', 'Время перезвона', 'Информация из CRM',
                 'Ответственный из CRM'])
    # добавим нужные столбы
    new_data['Дозвон'] = [1 if duration > 10 and status == 'Отвечен' else 0 for duration, status in
                          zip(new_data['Длительность звонка'], new_data['Статус'])]
    new_data['Звонок'] = 1
    return new_data
