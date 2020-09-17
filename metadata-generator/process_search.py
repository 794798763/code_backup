import requests
# files=[]
# files.append({"hash":"11new19999yuihjvbn",
#               'size':2048})
# files.append({"hash":"11new22ucy",
#              'size':2048})
# files.append({"hash":"11new32184hbu",
#              'size':2048})
# files.append({"hash":"11new42765g",
#              'size':2048})
# files.append({"hash":"11new52-966fs",
#              'size':2048})


files=[]
files.append({"hash":"xxx11new22ucy",
             'size':20480})
files.append({"hash":"xxx11new32184hbu",
             'size':20480})
files.append({"hash":"xxx9595951",
             'size':20480})
para={'files':files}
r2=requests.get(url="http://localhost:8008/searchForFile",
    json=para)
print(r2.json())
