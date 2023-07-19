import requests
import hashlib

user='051340'
url = f'https://sipuni.com/api/statistic/export/all'
hash = hashlib.md5(user.encode()).hexdigest()
# response=requests.get(url,data=hash)
url2 = f'https://sipuni.com/api/statistic/export/all?user={user}hash={hash}'
print(url2)
result=requests.get(url)
print(result.status_code)


