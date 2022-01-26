import requests

BASE = 'http://127.0.0.1:5000/'

data = [
    {'name': 'mommy',
     'likes': 1000,
     'views': 1000},
     {'name': 'kenith',
     'likes': 10,
     'views': 0},
     {'name': 'kevin',
     'likes': 10,
     'views': 100}
]

for i in range(len(data)):
    response = requests.get(BASE + f'video/{i}', data[i])
    print(response.json())
input()
response = requests.delete(BASE + "video/1")
print(response.json())