import requests
import hashlib

user = '051340'
limit = 1000
order = 'desc'
page = 1
secret = '0.njnaxjoq79'

hash_string = '+'.join([str(limit), order, str(page), user, secret])
hash_value = hashlib.md5(hash_string.encode()).hexdigest()
url = 'https://sipuni.com/api/statistic/export/all'

payload = {
    'limit': limit,
    'order': order,
    'page': page,
    'user': user,
    'hash': hash_value
}
response = requests.post(url, data=payload)
print(response.status_code)

with open(f'stat_{page}.csv', 'wb') as file:
    file.write(response.content)
