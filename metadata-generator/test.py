




#
# import json
# import requests
# files=[]
# files.append({"name":"yuihjvbn"})
# files.append({"name":"ucy"})
# files.append({"name":"seftcygv",'type':'directory','size':5231})
# files.append({"name":"184hbu"})
# files.append({"name":"765g"})
# files.append({"name":"-966fs"})
# para={'files':files}
# para['license']={'targets':['8001','8002','8003'],'hash':'rfytyuhbjnkm98456'}
# r1 = requests.post(
#     url="http://127.0.0.1:8001/test2",
    #json=para

# )
# print(r1.json())
#



# inpeers = []
# bwd = {}
# s = 'ws://192.168.255.246:8001-102400,ws://192.168.255.246:8002-20480'
# sl = s.split(',')
# for i in sl:
#     temp = i.split('-')
#     inpeers.append(temp[0])
#     bwd[temp[0]] = int(temp[1])
# print(inpeers)
# print(bwd)





# from Crypto.Hash import SHA256
# ll=[]
# ll.append("everyNode")
# print(str(0) + "0"+ str(1465154705) +"my genesis block!!"+str(ll))
# tt=SHA256.new(data=(str(0) + "0"+ str(1465154705) +"my genesis block!!"+str(ll)).encode()).hexdigest()
# print(tt)


# import websockets
# import json as JSON
# import time
#
# ws = websockets.connect("ws://localhost:3001")
#
# print(ws)

# import datetime
# import time
# a=datetime.datetime.now().strftime('%d日 %H:%M:%S')
# b=time.time()
# time.sleep(2)
# c=str(time.time())
# print(b)
# print(c)
# )

bw_list=[[0, 933, 1199, 937, 1348, 1130, 1427, 1420, 1312, 1585],
         [933, 0, 1104, 1210, 1297, 1424, 1628, 0, 1593, 1628],
         [1199, 1104, 0, 1306, 1496, 1495, 1616, 1657, 1702, 1617],
         [937, 1210, 1306, 0, 1468, 0, 1568, 1483, 1821, 1469],
         [1348, 1297, 1496, 1468, 0, 1534, 1506, 1882, 1768, 1810],
         [1130, 1424, 1495, 0, 1534, 0, 1584, 1514, 1766, 1617],
         [1427, 1628, 1616, 1568, 1506, 1584, 0, 1812, 0, 1808],
         [1420, 0, 1657, 1483, 1882, 1514, 1812, 0, 1790, 2077],
         [1312, 1593, 1702, 1821, 1768, 1766, 0, 1790, 0, 1904],
         [1585, 1628, 1617, 1469, 1810, 1617, 1808, 2077, 1904, 0]]


total_service_output=[11291, 10817, 13192, 11262, 14109, 12064, 12949, 13635, 13656, 15515]

transmission_cost=[1138, 1188, 974, 1141, 911, 1065, 992, 942, 941, 828]


# 求transmission_cost
# sum=0
# for i in total_service_output:
#     sum=sum+i
# average=sum/10
# for i in total_service_output:
#     transmission_cost.append(round(1000*(average/i)))
# print(transmission_cost)

#求total_service_output
# ls=[]
# for i in bw_list:
#     sum=0
#     for ii in i:
#         sum=sum+ii
#     ls.append(sum)
# print(ls)