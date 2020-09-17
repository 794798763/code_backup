import json
import requests
files=[]
# files.append({"hash":"11new19999yuihjvbn",
#               'size':20480})
files.append({"hash":"xxx11new22ucy",
             'size':2048})
files.append({"hash":"xxx11new32184hbu",
             'size':2048})
files.append({"hash":"xxx9595951",
             'size':2048})
# files.append({"hash":"11new52-966fs",
#              'size':2048})
para={'files':files}
para['license']={'targets':['8001','8003','8004','8005'],'hash':'9uhbjnasfd456'}
r1 = requests.post(
    url="http://127.0.0.1:8002/save",
    json=para
)
print(r1.json())