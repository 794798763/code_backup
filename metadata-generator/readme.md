# 数据结构

+ 
  storage_state_dic

```
    storage_state['storage_total']=storage_total
    storage_state['storage_consumed']=storage_consumed
    storage_state['usability']=usability
    storage_state['utilization_rate']=utilization_rate
    storage_state_dic[node_port]=storage_state
return storage_state_dic
```

+ storage_state_list

  由storage_state_dic构成的list

# 函数方法
向节点使用request进行save命令的时候,带宽不能太小,否则会超时

生成的图,print(graph_generator(10,1024,800))

十个节点,平均值500,标准差300,产生白噪声,再加上每个节点的基础服务能力,从节点一到节点10分别是:

200,400,600,...

生成的白噪声是

[[279], [443, 488], [297, 445, 376], [413, 462, 493, 620], [399, 621, 511, 222, 470], [525, 300, 559, 614, 600, 476], [536, 423, 496, 353, 403, 406, 497], [477, 513, 459, 358, 641, 353, 665, 441], [502, 506, 492, 528, 397, 548, 376, 494, 403], [445, 568, 431, 504, 489, 663, 689, 367, 784, 378]]

最终结果是:

```
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
```



## 求传输代价换了新的方法

传输代价=系数(暂用的是1000)*所有节点单位时间提供的服务能力和的平均值/当前节点单位时间提供的服务能力和