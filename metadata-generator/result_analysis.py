import time

import requests
import json as JSON
import datetime
import random
import numpy as np
node_port_list=['8001','8002','8003','8004','8005','8006','8007','8008','8009','8010']
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

def get_storage_state_dic():
    #获取每个节点的存储消耗情况
    storage_state_dic={}
    for node_port in node_port_list:
        storage_state={}
        target_url="http://localhost:"+node_port+"/getStorageState"
        r2=requests.get(url=target_url)
        r_j=JSON.loads(r2.json())
        storage_total=int(r_j['storage_total'])
        storage_consumed=r_j['storage_consumed']
        usability=True
        if storage_total<storage_consumed:
            usability=False
        utilization_rate=round(storage_consumed/float(storage_total),3)
        storage_state['storage_total']=storage_total
        storage_state['storage_consumed']=storage_consumed
        storage_state['usability']=usability
        storage_state['utilization_rate']=utilization_rate
        storage_state_dic[node_port]=storage_state
    return storage_state_dic

def storage_state_evaluate(storage_state_list):
    #在调用get_storage_state_dic函数后,对该函数的结果进行图形化表示,暂时用不到
    return False

def file_backup_efficiency_evaluate():
    #获取当前时间之前所有文件在备份时的时间花销
    file_evaluate_result_dic={}
    for node_port in node_port_list:
        target_url="http://localhost:"+node_port+"/getHistory"
        r2=requests.get(url=target_url)
        r_j=JSON.loads(r2.json())
        for history in r_j['history']:
            #根据该条历史更新评估字典中对应文件的记录
            file_hash=history['file_hash']
            if history['task_type']=='back_up_begin':
                if file_hash in file_evaluate_result_dic.keys():
                    if history['timestamp']<file_evaluate_result_dic[file_hash]['timestamp_begin']:
                        file_evaluate_result_dic[file_hash]['timestamp_begin']=history['timestamp']
                else:
                    temp_dic={}
                    temp_dic['timestamp_begin']=history['timestamp']
                    temp_dic['timestamp_success']=0
                    file_evaluate_result_dic[file_hash]=temp_dic
            elif history['task_type']=='back_up_success':
                if file_hash in file_evaluate_result_dic.keys():
                    if history['timestamp']>file_evaluate_result_dic[file_hash]['timestamp_success']:
                        file_evaluate_result_dic[file_hash]['timestamp_success']=history['timestamp']
                else:
                    temp_dic={}
                    temp_dic['timestamp_begin']=100000
                    temp_dic['timestamp_success']=history['timestamp']
                    file_evaluate_result_dic[file_hash]=temp_dic
    for i in file_evaluate_result_dic.keys():
        file_evaluate_result_dic[i]['time_consumed']=round(file_evaluate_result_dic[i]['timestamp_success']-file_evaluate_result_dic[i]['timestamp_begin'],2)
    return file_evaluate_result_dic

def get_all_history():
    total_history_dic={}
    for node_port in node_port_list:
        target_url="http://localhost:"+node_port+"/getHistory"
        r2=requests.get(url=target_url)
        r_j=JSON.loads(r2.json())
        total_history_dic[node_port]= r_j['history']
    return total_history_dic

def file_search_efficiency_evaluate(initiating_port):
    #获取当前时间之前的所有文件查询操作产生的时间花销
    file_evaluate_result_dic={}
    target_url="http://localhost:"+initiating_port+"/getHistory"
    r2=requests.get(url=target_url)
    r_j=JSON.loads(r2.json())
    for history in r_j['history']:
        file_hash=history['file_hash']
        if history['task_type'] == 'search_begin':
            if file_hash in file_evaluate_result_dic.keys():
                if history['timestamp'] < file_evaluate_result_dic[file_hash]['timestamp_begin']:
                    file_evaluate_result_dic[file_hash]['timestamp_begin'] = history['timestamp']
            else:
                temp_dic = {}
                temp_dic['timestamp_begin'] = history['timestamp']
                temp_dic['timestamp_success'] = 0.0
                file_evaluate_result_dic[file_hash] = temp_dic
        elif history['task_type'] == 'search_success':
            if file_hash in file_evaluate_result_dic.keys():
                if history['timestamp'] > file_evaluate_result_dic[file_hash]['timestamp_success']:
                    file_evaluate_result_dic[file_hash]['timestamp_success'] = history['timestamp']
                    file_evaluate_result_dic[file_hash]['source_port'] = history['target_port']
            else:
                temp_dic = {}
                temp_dic['timestamp_begin'] = 100000
                temp_dic['timestamp_success'] = history['timestamp']
                temp_dic['source_port'] = history['target_port']
                file_evaluate_result_dic[file_hash] = temp_dic
    for i in file_evaluate_result_dic.keys():
        file_evaluate_result_dic[i]['time_consumed']=round(file_evaluate_result_dic[i]['timestamp_success']-file_evaluate_result_dic[i]['timestamp_begin'],2)
    return file_evaluate_result_dic


#用来产生特定大小的文件的方法,返回一个dic,其key是产生的文件哈希,value 是一个list,里面放着该文件被拆分成的诸多文件块.
def file_generator(file_number_wanna_generated):
    #每个文件10Mb,被切分成5个2MB的文件碎片
    result_dic={}
    for i in range(file_number_wanna_generated):
        prefix_time=datetime.datetime.now().strftime('%H%M%S_')
        file_hash=prefix_time+''.join(random.sample('zyxwvutsrqponmlkjihgfedcba',8))
        list_temp=[]
        for ii in range(5):
            piece={}
            piece['hash']=prefix_time+str(ii)+"_"+''.join(random.sample('zyxwvutsrqponmlkjihgfedcba',8))
            piece['size']=2048
            list_temp.append(piece)
        result_dic[file_hash]=list_temp
    return result_dic



def file_retention(file_dic):
    with open("files.json", "a") as f:
        f.write(JSON.dumps(file_dic))

def file_placement(file_dic,business_node_port,target_port_list):
    for key in file_dic.keys():
        l=file_dic[key]
        para = {'files': l}
        para['license'] = {'targets': target_port_list, 'hash': '9uhbjnasfd456'}
        r1 = requests.post(
            url="http://127.0.0.1:"+business_node_port+"/save",
            json=para

        )
        print(r1.json())
        time.sleep(2)
        #要注意每次请求都间隔了两秒
    return True

def graph_generator(node_number,bindwidth_average,bindwidth_standard_deviation):
    result=[]
    for num in range(node_number+1):
        if not num==0:
            s = np.random.normal(bindwidth_average, bindwidth_standard_deviation, num)
            r=[]
            for ss in s:
                r.append(round(ss))
            result.append(r)
    return result


    # f=file_generator(1)
    # file_retention(f)
    # file_placement(f,'8002',['8003','8004'])

    # print(get_all_history())
    # print(file_search_efficiency_evaluate('8008'))

    # print(get_storage_state_dic())
    # print(graph_generator(10,1024,800))

def select_random():
    random_port_list=random.sample(node_port_list,3)
    return random_port_list

def select_costtable():
    business_volume_coefficient=1
    storage_cost_dic=calculate_storage_cost()
    storage_cost_list=[]
    cost_list_final=[]
    for port in node_port_list:
        storage_cost_list.append(storage_cost_dic[port])
    for i in range(10):
        c=transmission_cost[i]*business_volume_coefficient+storage_cost_list[i]
        cost_list_final.append(c)
    min_it=0
    min=999999
    second_it=0
    second=999999
    thrid_it=0
    thrid=999999
    for i in range(10):
        if cost_list_final[i]<min:
            min=cost_list_final[i]
            min_it=i
    for i in range(10):
        if cost_list_final[i]<second and not i==min_it:
            second=cost_list_final[i]
            second_it=i
    for i in range(10):
        if cost_list_final[i]<thrid and not i==min_it and not i==second_it:
            thrid=cost_list_final[i]
            thrid_it=i
    return [str(min_it+1+8000),str(second_it+1+8000),str(thrid_it+1+8000)]





#每次存储10M文件并显示,直到有点存储空间耗尽
def experiment2_random():
    flag=True
    x=0
    while flag:
        x=x+1
        backup_port_list =select_random()
        f=file_generator(1)
        file_retention(f)
        file_placement(f,backup_port_list[1],backup_port_list)
        time.sleep(2)
        storage_state_dic=get_storage_state_dic()
        record={x:storage_state_dic}
        print(record)
        for key in storage_state_dic.keys():
            if not storage_state_dic[key]['usability']:
                return

def experiment2_costtable():
    x=0
    while True:
        x=x+1
        backup_port_list =select_costtable()
        f=file_generator(1)
        file_retention(f)
        file_placement(f,backup_port_list[1],backup_port_list)
        time.sleep(2)
        storage_state_dic=get_storage_state_dic()
        record={x:storage_state_dic}
        print(record)
        for key in storage_state_dic.keys():
            if not storage_state_dic[key]['usability']:
                return



def calculate_storage_cost():
    sd=get_storage_state_dic()
    re={}
    for key in sd.keys():
        state=sd[key]
        storage_total=state['storage_total']
        storage_consumed=state['storage_consumed']
        storage_cost=1000*storage_consumed/storage_total
        if storage_cost>1000:
            re[key] = 1000
        else:
            re[key]=round(storage_cost)
    return re



def  experiment3_random():
    f = file_generator(2)
    file_retention(f)
    result={}
    for filehash in f.keys():
        backup_port_list =select_random()
        para = {'files': f[filehash]}
        para['license'] = {'targets': backup_port_list, 'hash': '9uhbjnasfd456'}
        r1 = requests.post(
            url="http://127.0.0.1:"+backup_port_list[1]+"/save",
            json=para

        )
        print(r1.json())
        time.sleep(1)
    for filehash in f.keys():
        search_port=random.sample(node_port_list, 1)[0]
        print('search_port='+search_port)
        para = {'files': f[filehash]}
        r2 = requests.get(url="http://localhost:"+search_port+"/searchForFile",
                          json=para)
        print(r2.json())
        time.sleep(3)
        time_begin=99999999
        time_end=0
        result_dic=file_search_efficiency_evaluate(search_port)
        for piece in f[filehash]:
            rec=result_dic[piece['hash']]
            if time_begin>rec['timestamp_begin']:
                time_begin=rec['timestamp_begin']
            if time_end<rec['timestamp_success']:
                time_end=rec['timestamp_success']
        result[filehash]=round(time_end-time_begin,2)
    return result








# print(get_storage_state_dic())
# print(file_backup_efficiency_evaluate())
print(experiment3_random())
# print(experiment2_costtable())
# print(file_search_efficiency_evaluate('8006'))