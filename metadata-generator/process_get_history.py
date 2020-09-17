import requests
r2=requests.get(url="http://localhost:8008/getHistory")
print(r2.json())



