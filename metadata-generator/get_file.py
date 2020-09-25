import requests
# r2=requests.get(url="http://localhost:8006/getAllFilesLocal")
r2=requests.get(url="http://localhost:8002/peers")
print(r2.json())
