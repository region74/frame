from datetime import datetime
import requests
from api.config import data
import asyncio


# функция обращается по api и получает csv файл
async def get_data():
    api_url = 'https://sipuni.com/api/statistic/export'
    try:
        response = requests.post(api_url, data=data)
        if response.status_code == 200:
            with open(f"data.csv", 'wb') as file:
                file.write(response.content)
        else:
            with open('api.log', 'a', encoding='utf-8') as file:
                file.write(f'{datetime.now()} {response.status_code}\n')
    except Exception as e:
        with open('api.log', 'a', encoding='utf-8') as file:
            file.write(f'{datetime.now()} {str(e)}\n')


def main():
    asyncio.run(get_data())


main()
