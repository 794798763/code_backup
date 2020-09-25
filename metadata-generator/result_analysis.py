import time
import sys
from queue import Queue

import numpy as np
import math
import copy

from scipy.optimize import linprog
import requests
import json as JSON
import datetime
import random
import numpy as np
node_port_list=['8001','8002','8003','8004','8005','8006','8007','8008','8009','8010']
bw_list=[[0, 983, 899, 925, 1505, 1252, 1871, 2137, 2171, 2508],
        [983, 0, 1620, 1489, 1256, 1502, 1801, 0, 2669, 2626],
         [899, 1620, 0, 2020, 1656, 2071, 2289, 2289, 2457, 2656],
        [925, 1489, 2020, 0, 1725, 2438, 2605, 2838, 2502, 2680],
         [1505, 1256, 1656, 1725, 0, 0, 2572, 2452, 3108, 3521],
        [1252, 1502, 2071, 2438, 0, 0, 0, 2656, 0, 3583],
         [1871, 1801, 2289, 2605, 2572, 0, 0, 3504, 0, 3499],
         [2137, 0, 2289, 2838, 2452, 2656, 3504, 0, 3671, 3502],
         [2171, 2669, 2457, 2502, 3108, 0, 0, 3671, 0, 3936],
         [2508, 2626, 2656, 2680, 3521, 3583, 3499, 3502, 3936, 0]]
trans_cost_table=[[0, 104, 114, 111, 68, 82, 55, 48, 47, 41],
                  [104, 0, 63, 69, 82, 68, 57, -1, 38, 39],
                  [114, 63, 0, 51, 62, 49, 45, 45, 42, 39],
                  [111, 69, 51, 0, 59, 42, 39, 36, 41, 38],
                  [68, 82, 62, 59, 0, -1, 40, 42, 33, 29],
                  [82, 68, 49, 42, -1, 0, -1, 39, -1, 29],
                  [55, 57, 45, 39, 40, -1, 0, 29, -1, 29],
                  [48, -1, 45, 36, 42, 39, 29, 0, 28, 29],
                  [47, 38, 42, 41, 33, -1, -1, 28, 0, 26],
                  [41, 39, 39, 38, 29, 29, 29, 29, 26, 0]]



total_service_output=[14251, 13946, 17957, 19222, 17795, 13502, 18141, 23049, 20514, 28511]

transmission_cost=[1311, 1340, 1041, 972, 1050, 1384, 1030, 811, 911, 655]

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
            piece['size']=512
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
        time.sleep(1)
        #要注意每次请求都间隔了两秒
    return True

def graph_generator():
    list=[]
    for i in range(10):
        l=[]
        for j in range(10):
            l.append(i*200+j*200)
        list.append(l)
    s = np.random.normal(500, 300, 50)
    ss=s.tolist()
    for i in range(10):
        for j in range(10):
            if i < j:
                list[i][j]=list[i][j]+random.sample(ss,3)[1]
                if round(random.sample(ss,3)[1])%20==5:
                    list[i][j]=0
            if i==j:
                list[i][j] = 0
            if i>j:
                list[i][j]=list[j][i]
    for i in range(10):
        for j in range(10):
            list[i][j] = round(list[i][j])
    print(list)

def total_service_output_generator():
    l=[]
    for i in bw_list:
        sum=0
        for j in i:
            sum=sum+j
        l.append(sum)
    print(l)

def transmission_cost_generator():
    sum=0
    l=[]
    for i in total_service_output:
        sum=sum+i
    av=sum/10
    for i in total_service_output:
        l.append(round(av/i*1000))
    print(l)

def select_random():
    random_port_list=random.sample(node_port_list,3)
    return random_port_list

def select_costtable(ks):
    business_volume_coefficient=1
    storage_cost_dic=calculate_storage_cost(ks)
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
        if storage_cost_list[i]>=ks:
            continue
        if cost_list_final[i]<min:
            min=cost_list_final[i]
            min_it=i
    for i in range(10):
        if storage_cost_list[i]>=ks:
            continue
        if cost_list_final[i]<second and not i==min_it:
            second=cost_list_final[i]
            second_it=i
    for i in range(10):
        if storage_cost_list[i]>=ks:
            continue
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
        time.sleep(0.5)
        storage_state_dic=get_storage_state_dic()
        record={x:storage_state_dic}
        print(record)
        for key in storage_state_dic.keys():
            if not storage_state_dic[key]['usability']:
                return

def experiment2_costtable():
    #实验二,不停存储直到有节点被存爆,此时查看最低存储率
    x=0
    while True:
        x=x+1
        backup_port_list =select_costtable(20000)
        f=file_generator(1)
        file_retention(f)
        file_placement(f,backup_port_list[1],backup_port_list)
        time.sleep(1)
        storage_state_dic=get_storage_state_dic()
        record={x:storage_state_dic}
        print(record)
        for key in storage_state_dic.keys():
            if not storage_state_dic[key]['usability']:
                return



def calculate_storage_cost(ks):
    sd=get_storage_state_dic()
    re={}
    for key in sd.keys():
        state=sd[key]
        storage_total=state['storage_total']
        storage_consumed=state['storage_consumed']
        storage_cost=ks*storage_consumed/storage_total
        if storage_cost>ks:
            re[key] = ks
        else:
            re[key]=round(storage_cost)
    return re



def  experiment3_random():
    f = file_generator(50)
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
        search_port='8001'
        para = {'files': f[filehash]}
        r2 = requests.get(url="http://localhost:"+search_port+"/searchForFile",
                          json=para)
        print(r2.json())
        time.sleep(2)
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


def  experiment3_costtable():
    #存储文件然后进行访问,分析访问结果查看访问效率
    f = file_generator(20)
    file_retention(f)
    result={}
    for filehash in f.keys():
        backup_port_list =select_costtable(2000)
        para = {'files': f[filehash]}
        para['license'] = {'targets': backup_port_list, 'hash': '9uhbjnasfd456'}
        r1 = requests.post(
            url="http://127.0.0.1:"+backup_port_list[0]+"/save",
            json=para

        )
        time.sleep(0.5)
    for filehash in f.keys():
        search_port='8001'
        para = {'files': f[filehash]}
        r2 = requests.get(url="http://localhost:"+search_port+"/searchForFile",
                          json=para)
        time.sleep(1)
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

#####################################################################################
def columDel(gragh, r,openCondition):
    condition = copy.deepcopy(gragh)
    # 设置能够在半径范围内覆盖的节点
    for i in range(len(gragh)):
        for j in range(len(gragh[i])):
            if gragh[i][j] <= r and gragh[i][j] != -1:
                condition[i][j] = 1
            else:
                condition[i][j] = 0
    # print("初始问题的方程组是", condition)
    # 判断方程组之间的包含关系，若包含，则将对应位置的元素值置零，得到初始简化后的方程组
    len1 = len(condition[0])
    imd = [1] * len1
    lis = []
    for i in range(len(condition)):
        l = []
        for j in range(len(condition[i])):
            if condition[i][j] == 1:
                l.append(j)
        lis.append(l)
    for i in range(len(lis)):
        for j in range(len(lis)):
            if set(lis[i]) < set(lis[j]):
                openCondition[i] = 0
                imd[i] = 0
    # print(" imd=",imd)
    for i in range(len(condition)):
        for j in range(len(condition[i])):
            condition[i][j] = condition[i][j] & imd[j]
    print(condition)
    return judge(condition,openCondition)

def judge(condition,openCondition):
    # 判断简化后的元素方程组是否只包含1个元素，若只包含一个元素，则表示对应节点开放，并且将包含有这个元素的方程组删除
    for i in range(len(condition)):
        if sum(condition[i]) == 1:
            index = list(condition[i]).index(1)
            openCondition[index] = 1
            for j in range(len(condition)):
                if condition[j][index] == 1:
                    condition[j] = [0] * len(condition[i])
    # 对得到的方程组去重操作
    # print("去除一个元素后的方程组",condition)
    restLis = []
    # print(restLis)
    for node in condition:
        flag = 1
        # print("长度是",len(restLis))
        for i in range(len(restLis)):
            # print("当前循环进入次/数",i)
            if list(node) == restLis[i]:
                # print("两者之间相同")
                flag = 0
                break;
        if flag and sum(node) != 0:
            restLis.append(list(node))
    if len(restLis) == 0: #当前方程式全部得到解，不包含未解决的方程式，将待定open的节点直接不open
        for i in range(len(openCondition)):
            if openCondition[i] == -1:
                openCondition[i] = 0
        return openCondition,1
    # print("消元之后的方程组",restLis)
    # print("消元之后的节点开放情况",openCondition)
    return  openCondition,restLis

def rowDel(restLis,openCondition):
    # print(" 经历过列消元之后的方程组 restList=",restLis," 其类型是",type(restLis))
    lis = []
    for i in range(len(restLis)):
        l = []
        for j in range(len(restLis[i])):
            if restLis[i][j] == 1:
                l.append(j)
        lis.append(l)
    # print("行归一化后的方程组",lis)
    #得到行删减后的方程组nowProblem
    jjj = [1]*len(restLis)
    # print("j = ",jjj)
    for i in range(len(lis)):
        for j in range(len(lis)):
            if set(lis[i]) < set(lis[j]):
                jjj[i] = 0
    rest = []
    for i in range(len(restLis)):
        if jjj[i] == 1:
            rest.append(restLis[i])
    # print("行删减后的方程组",rest)
    return judge(rest,openCondition)


class ILP():
    def __init__(self, c, A_ub, b_ub, A_eq, b_eq, bounds,t):
        # 全局参数
        self.LOWER_BOUND = -sys.maxsize
        self.UPPER_BOUND = sys.maxsize
        self.opt_val = None
        self.opt_x = None
        self.Q = Queue()
        # 这些参数在每轮计算中都不会改变
        self.c = c
        self.A_eq = A_eq
        self.b_eq = b_eq
        self.bounds = bounds
        self.t = t

        # 首先计算一下初始问题
        r = linprog(c, A_ub, b_ub, A_eq, b_eq, bounds,method='revised simplex')

        # 若最初问题线性不可解
        if not r.success:
            raise ValueError('Not a feasible problem!')

        # 将解和约束参数放入队列
        # print("初始化的解是",r.fun," 初始化变量取值是",r.x)
        self.Q.put((r, A_ub, b_ub))

    def solve(self):
        while not self.Q.empty():
            # print("开始一次新的循环")
            # 取出当前问题
            res, A_ub, b_ub = self.Q.get(block=False)
            # print("当前问题的系数矩阵是",A_ub," 常数矩阵：",b_ub)
            # print("当前问题的一般解是",res.fun," 变量取值：",res.x)
            # 当前最优值小于总下界，则排除此区域
            # print("当前全局最优值是：",self.opt_val," 当前全局最优解是：",self.opt_x," 当前下界是：",self.UPPER_BOUND)
            if res.fun > self.UPPER_BOUND:
                continue

            # 若结果 x 中全为整数，则尝试更新全局下界、全局最优值和最优解
            if all(((x-math.floor(x))<self.t or (math.ceil(x)-x)<self.t) for x in res.x):
                # print("#####################解是整数####################################")
                # print(" 为整数时的解，",res.fun)
                if self.UPPER_BOUND < res.fun:
                    self.UPPER_BOUND = res.fun
                if self.opt_val is None or self.opt_val < res.fun:
                    self.opt_val = res.fun
                    self.opt_x = res.x
                # print("此时包含全局最优解，全局最优值是",self.opt_val," 全局最优值的解是，",self.opt_x)
                continue

            # 进行分枝
            else:
                # 寻找 x 中第一个不是整数的，取其下标 idx
                # print("x0 = ",res.x[0])
                # print("x1 = ",res.x[1])
                idx = [i for i, x in enumerate(res.x) if (x - math.floor(x)) > self.t and (math.ceil(x) - x) > self.t][0]
                # print("第",idx,"的取值不是整数")
                # 构建新的约束条件（分割
                new_con1 = np.zeros(A_ub.shape[1])
                new_con1[idx] = -1
                new_con2 = np.zeros(A_ub.shape[1])
                new_con2[idx] = 1
                new_A_ub1 = np.insert(A_ub, A_ub.shape[0], new_con1, axis=0)
                new_A_ub2 = np.insert(A_ub, A_ub.shape[0], new_con2, axis=0)
                new_b_ub1 = np.insert(
                    b_ub, b_ub.shape[0], -math.ceil(res.x[idx]), axis=0)
                new_b_ub2 = np.insert(
                    b_ub, b_ub.shape[0], math.floor(res.x[idx]), axis=0)
                # print("#############################")
                # print("分支1的系数矩阵是",new_A_ub1,' 常数矩阵是：',new_b_ub1)
                # print("#############################")
                # print("分支2的系数矩阵是", new_A_ub2, ' 常数矩阵是：', new_b_ub2)
                # 将新约束条件加入队列，先加最优值大的那一支
                r1 = linprog(self.c, new_A_ub1, new_b_ub1, self.A_eq,
                             self.b_eq, self.bounds,method='revised simplex')
                r2 = linprog(self.c, new_A_ub2, new_b_ub2, self.A_eq,
                             self.b_eq, self.bounds,method='revised simplex')
                if not r1.success and r2.success:
                    self.Q.put((r2, new_A_ub2, new_b_ub2))
                elif not r2.success and r1.success:
                    self.Q.put((r1, new_A_ub1, new_b_ub1))
                elif r1.success and r2.success:
                    # print(" 1分支的最优值：",r1.fun," 2分支的最优值：",r2.fun)
                    if r1.fun > r2.fun:
                        self.Q.put((r1, new_A_ub1, new_b_ub1))
                        self.Q.put((r2, new_A_ub2, new_b_ub2))
                    else:
                        self.Q.put((r2, new_A_ub2, new_b_ub2))
                        self.Q.put((r1, new_A_ub1, new_b_ub1))
def solveCoveringProblem(graph,r,openCondition,cost):
    rest = columDel(graph, r,openCondition)
    # print("列消除后的方程组",rest)
    if rest[1] == 1:
        totalOpenNum = sum(openCondition)
        return openCondition, totalOpenNum
    else:
        # print("执行列删除结束，并且包涵有未确定的节点")
        # print(rest[0], rest[1])
        rowRest = rowDel(rest[1], rest[0])
        if rowRest[1] == 1:
            print("执行rowDel结束，得到有效解")
            # print(rowRest[0], rowRest[1])
        else:
            # print("执行rowDel结束，仍然没有有效解，继续使用分支界定法求解")
            # print("当前剩余方程组是：", rowRest[1], "当前节点开放情况是：", rowRest[0])
            t = 1.0E-6
            Aeq = None
            Aeq = None
            beq = None
            c = cost
            A = -np.array(rowRest[1])
            b = -np.ones(len(rowRest[1]), dtype=int)
            vlen = len(rowRest[0])
            bounds = []
            for i in range(vlen):
                bounds.append((0, 1))
            solver = ILP(c, A, b, Aeq, beq, bounds, t)
            solver.solve()
            # print("使用分支界定法的结果：", " 问题最优值=",solver.opt_val, "问题最优解=",solver.opt_x)
            c = solver.opt_x.astype(int)
            for i in range(len(c)):
                if c[i] == 1:
                    openCondition[i] = 1
                else:
                    if openCondition[i] == -1:
                        openCondition[i] = 0
            # print("the openCondition is ",openCondition)
    totalOpenNum = sum(openCondition)
    return openCondition,totalOpenNum
def solveCenterProblem(graph,p,cost):
    maxLink = np.max(graph)  # 整个元素列组中的最大值
    # condition = copy.deepcopy(gragh)
    openCondition = [-1] * len(graph[0])  # 初始不开设所有的工厂
    RL = 0
    RH = (len(graph[0]) - 1) * maxLink
    while (RL != RH):

        r = math.floor((RL + RH) / 2)
        result = solveCoveringProblem(graph, r,openCondition,cost)
        # nowOpenCondition = result[0]
        nowTotalOpenNum = result[1]
        print(" 集合覆盖问题的解是：",result)
        print("RL= ",RL," RH=",RH," r=",r," qr=",nowTotalOpenNum)
        if nowTotalOpenNum <= p:
            RH = r
        else:
            RL = r + 1
    return RH

def select_center_problem():
    p=3
    gragh = np.array(trans_cost_table)
    cost_dic = calculate_storage_cost(500) # n个设施节点的开放代价
    cost=[]
    for i in node_port_list:
        cost.append(cost_dic[i])
    openCondition = [-1] * len(gragh[0])  # 初始不开设所有的工厂
    r = solveCenterProblem(gragh,p,cost)
    print("覆盖半径",r)
    re = solveCoveringProblem(gragh,r,openCondition,cost)
    print("re =",re)
    return re

#######################################################################################3


def experiment2_center_problem():
    #实验二,不停存储直到有节点被存爆,此时查看最低存储率
    x=0
    while True:
        x=x+1
        select_result_list ,_=select_center_problem()
        backup_port_list=[]
        f=file_generator(1)
        file_retention(f)
        for i in range(len(select_result_list)):
            if not select_result_list[i]==0:
                backup_port_list.append(str(i+1+8000))
        file_placement(f,backup_port_list[0],backup_port_list)
        time.sleep(0.5)
        storage_state_dic=get_storage_state_dic()
        record={x:storage_state_dic}
        print(record)
        for key in storage_state_dic.keys():
            if not storage_state_dic[key]['usability']:
                return

# print(get_storage_state_dic())
# print(file_backup_efficiency_evaluate())
# re=experiment3_random()
############################################
# index_list=[]
# val_list=[]
# for i in range(100):
#     re=experiment3_costtable()
#     count=0
#     sum=0
#     for val in re.values():
#         if not val==0:
#             count=count+1
#             sum=sum+val
#     index_list.append((i+1)*20)
#     val_list.append(round(sum/count,3))
#     print('平均访问时间是: '+str(sum/count))
#     print(re)
#     print(index_list)
#     print(val_list)
###############################################
def experiment4_costtable():
    #实验二,不停存储直到node5被激活,查看其他节点存储情况
    x=0
    count=0
    index=[]
    storage_node1=[]
    storage_node2=[]
    storage_node3=[]
    storage_node4=[]
    storage_node5=[]
    storage_node6=[]
    storage_node7=[]
    storage_node8=[]
    storage_node9=[]
    storage_node10=[]
    while True:
        x=x+1
        backup_port_list =select_costtable(2000)
        f=file_generator(1)
        file_retention(f)
        file_placement(f,backup_port_list[1],backup_port_list)
        storage_state_dic=get_storage_state_dic()
        index.append(x)
        storage_node1.append(round(storage_state_dic['8001']['utilization_rate'],3))
        storage_node2.append(round(storage_state_dic['8002']['utilization_rate'],3))
        storage_node3.append(round(storage_state_dic['8003']['utilization_rate'],3))
        storage_node4.append(round(storage_state_dic['8004']['utilization_rate'],3))
        storage_node5.append(round(storage_state_dic['8005']['utilization_rate'],3))
        storage_node6.append(round(storage_state_dic['8006']['utilization_rate'],3))
        storage_node7.append(round(storage_state_dic['8007']['utilization_rate'],3))
        storage_node8.append(round(storage_state_dic['8008']['utilization_rate'],3))
        storage_node9.append(round(storage_state_dic['8009']['utilization_rate'],3))
        storage_node10.append(round(storage_state_dic['8010']['utilization_rate'],3))
        print('index='+str(index))
        print('node1='+str(storage_node1))
        print('node2='+str(storage_node2))
        print('node3='+str(storage_node3))
        print('node4='+str(storage_node4))
        print('node5='+str(storage_node5))
        print('node6='+str(storage_node6))
        print('node7='+str(storage_node7))
        print('node8='+str(storage_node8))
        print('node9='+str(storage_node9))
        print('node10='+str(storage_node10))
        if storage_state_dic['8005']['storage_consumed']>0:
            count=count+1
        if count==5:
            break


def get_storage_rate_node5():
    dicccc={}
    k=0.5
    for i in range(len(transmission_cost)):
        dicccc[str(8000+i+1)]=k*(transmission_cost[i]-1050)/1000
    print(dicccc)
# print(experiment2_costtable())
# print(experiment2_random())
print(experiment4_costtable())
# print(file_search_efficiency_evaluate('8006'))
# experiment2_center_problem()
# get_storage_rate_node5()