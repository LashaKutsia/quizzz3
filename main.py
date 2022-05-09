# import os
# os.system("pip install requests")
import json

import requests
key = '0484d2f1ceae50a691c68634ab21f46b'
city = input("დაასახელეთ ქალაქი: ")
resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key}')
print(resp.text)
print(resp.status_code)
print(resp.headers)
r = json.loads(resp.text)
with open('data.name', 'w')as file:
    json.dump(r, file, indent=4)


