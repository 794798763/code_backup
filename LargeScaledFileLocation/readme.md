# 大文件备份策略



-------------------------------------------------------在设置启动参数的时候 添加peers的时候,不只要用逗号隔开,还要给每一段设置初始带宽,比如
	ws://192.168.255.246:8001-102400,ws://192.168.255.246:8002-20480






​	
-------------------------------------------------------------建立init_socket的时候,先connect之后,要相互之间发送一条消息,沟通带宽大小-重写initi_connection
我们最初的设计是通过接收测试数据包的延迟测定贷款大小,这里我们直接给他初始化上,初始化的方法就是写docker-compose
-------------------------------------------------要写BANDWIDTH_COORDINATION的响应
​	message:{
​		type:"BANDWIDTH_COORDINATION",
​		size:""
​	}




--------------------------------------------------所以对于我们的区块链节点来说,我们有了延迟表,我们还需要发送request给每一个节点获得他们的存储情况,计算存储代价
论文设计中有一个从区块链接点发往每一个存储节点的测试消息,在文件传播的时候寻找最近的存储节点最先传输.实际中，我们可以给区块链节点直接初始化上
-----------------------------------------------------------正在写-----------在文件从区块链接点发往存储节点时候,request里面要包含文件信息(包括各个小文件块的名字,大小),需要存储的节点,以及区块链我们在初始化的时候设置的到每个节点的带宽.每个存储节点会根据对应的带宽计算传输用时.
	



现在已经能构成图结构了
	要在每个server里维护一个list 存放本节点存储的file
	file:{
		name:""
		type:"file/directory"
		order:""
		hash:""
		size:""	
	}
	其中一个文件被拆分成很多个file,许多个file有对应的顺序order ,通过directory能够进行引导和组装
	
	
	
	
	
	每个server还要维护一个带宽占用情况从ws1 到ws2  必须对应的带宽有剩余才可以	
	bandwidth:{
		ws1:102400
		ws2:20480
	}
	当带宽有剩余时,计算文件传输用时,然后设置延时,延时结束返回带宽


​	
​	
​	
​	
​	每一个server还要有一个全局变量，记录当前节点的存储空间使用情况。
​	remaining-space


​	
​	
​	
​	
​	
通过更改message里的type进行协作


​	
​	文件存储过程:
​	存储申请:
​	message:{
​		type:"STORAGE_APPLY"
​		filename:""
​		size:""
​	}


	 同意存储
	message:{
		type:"STORAGE_AGREE"
		
	}


​	
​	 开始传输
​	message:{
​		type:"TRANSMISSION_BEGIN"
​	}
​	开始传输后存储方开始计时，存储方存储完毕后返回完成的message，然后传输方开放对应的带宽


​	
​	完成传输
​	message:{
​		type:"TRANSMISSION_COMPLETE"
​		
​	}


​	
​	申请文件
​	message:{
​		type:"GAIN_APPLY"
​		name:""
​		
​	}


​	
​	申请文件
​	message:{
​		type:"GAIN_AGREE"
​		name:""
​		
​	}
​	发送同意之后,再发送TRANSMISSION_BEGIN


​	
​	
​	存储任务
​	message:{
​		type:"STORAGE_TASK"
​		file:[]
​		backup_location:[]
​		
​	}
​	在区块链结点有文件放置任务的时候用	


​	
​	
​	
​	
​	
​	
​	
​	
​	
​	
​	
​	
​	
​	

## 方法





## 数据属性





```
用来提供不是恶意存储的证明.现在只用了targets这个属性,用来保存都有谁需要保存这个文件.
license:{
	'targets':['3001',3002],
	'task_source':'',
	'signature':'',
	
}
```

```
	file:{
		name:""
		type:"file/directory"
		order:""
		hash:""
		size:""	
	}
```

sockets列表改成了字典型

## 过程

## 启动

根目录下:

```
docker-compose up
```

重新构建镜像需要:

```
docker-compose up --force-recreate --build
```

