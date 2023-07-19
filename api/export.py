import requests
import hashlib
from datetime import date
import urllib.parse

user = '051340'
from_date = date.today().strftime("%d.%m.%Y")
to_date = date.today().strftime("%d.%m.%Y")
type = '2'
state = '0'
tree = '000691234'
showTreeId = '0'
fromNumber = ''
toNumber = ''
numbersRinged = 0
numbersInvolved = 1
names = 1
outgoingLine = 1
toAnswer = ''
anonymous = '1'
firstTime = '0'
dtmfUserAnswer = '0'
hash = '0.njnaxjoq79'

hash_string = '+'.join(
    [anonymous, str(dtmfUserAnswer), firstTime, from_date, fromNumber, str(names), str(numbersInvolved),
     str(numbersRinged), str(outgoingLine), showTreeId, state, to_date, toAnswer, toNumber, tree, type, user, hash]
)

hash = hashlib.md5(hash_string.encode()).hexdigest()

url = 'https://sipuni.com/api/statistic/export'
data = {
    'anonymous': anonymous,
    'dtmfUserAnswer': dtmfUserAnswer,
    'firstTime': firstTime,
    'from': from_date,
    'fromNumber': fromNumber,
    'names': names,
    'numbersInvolved': numbersInvolved,
    'numbersRinged': numbersRinged,
    'outgoingLine': outgoingLine,
    'showTreeId': showTreeId,
    'state': state,
    'to': to_date,
    'toAnswer': toAnswer,
    'toNumber': toNumber,
    'tree': tree,
    'type': type,
    'user': user,
    'hash': hash,
}

response = requests.post(url, data=data)
print(response.status_code)

filename = f"stat_{from_date}-{to_date}.csv"
content_disposition = f"attachment; filename={filename}"
response_headers = {'Content-Disposition': content_disposition}

# Формируем URL-строку с GET-параметрами
url_with_params = 'https://sipuni.com/api/statistic/export?' + urllib.parse.urlencode(data)
print("Полный URL с параметрами:")
print(url_with_params)

with open(filename, 'wb') as file:
    file.write(response.content)
