import asyncio
import json as JSON
import os
import websockets
import time

from sanic import Sanic
from sanic.response import json
from websockets.exceptions import ConnectionClosed

from utils.logger import logger


QUERY_LATEST = 0
QUERY_ALL = 1
BANDWIDTH_COORDINATION=2
STORAGE_APPLY=3
GAIN_APPLY=4
SEARCH_FOR_FILE=5
PROVIDE_AGREE=6
TRANSMISSION_APPLY=7

try:
    sport = str(os.environ['SPORT'])
except KeyError as e:
    sport = '8001'

try:
    bwtn = int(os.environ['BWTN'])
except KeyError as e:
    bwtn = 1024
initialPeers = []
bwd={}
try:
    sl = os.environ['PEERS'].split(",")
    for i in sl:
        temp = i.split('-')
        initialPeers.append(temp[0])
        bwd[temp[0]] = int(temp[1])
except Exception as e:
    initialPeers = []


sever_location='127.0.0.1:'+str(sport)

class Server(object):
    def __init__(self):
        self.app = Sanic()  # 一种Python web框架
        self.sockets = dict() # 里面是websocket，可以当做TCP，维持链接，用socket进行通信
        self.files=[]
        self.flag=1
        self.sport=sport
        self.storage_total=104800
        self.storage_consumed=0
        self.band_width_dic=bwd
        self.locked_port=[]
        self.history=[]
        self.app.add_route(self.peers, '/peers', methods=['GET'])
        self.app.add_route(self.get_storage_state, '/getStorageState', methods=['GET'])
        self.app.add_route(self.get_all_files_local, '/getAllFilesLocal', methods=['GET'])
        self.app.add_route(self.search_for_file, '/searchForFile', methods=['GET'])
        self.app.add_route(self.add_peer, '/addPeer', methods=['POST'])
        self.app.add_route(self.save, '/save', methods=['POST'])
        self.app.add_websocket_route(self.p2p_handler, '/')
        self.app.add_route(self.get_history, '/getHistory', methods=['GET'])

    #李文全：2020.6.23：接口返回数据出错修正
    async def peers(self, request):
        # 从连接里解析数发送地址和接收地址
        # 返回所有的对等节点
        temp=[]
        for sk in self.sockets.keys():
            temp.append(sk)
        #result={"peers":temp}
        result={"peers":temp}
        return json(JSON.dumps(result))


    async def get_storage_state(self, request):
        result={"storage_total":self.storage_total}
        result['storage_consumed']=self.storage_consumed
        return json(JSON.dumps(result))

    #废弃
    async def add_peer(self, request):
        return json(JSON.dumps({"status": True}))



    async def get_history(self, request):
        return json(JSON.dumps({"history": self.history}))

    # initP2PServer WebSocket server
    async def p2p_handler(self, request, ws):
        logger.info('listening websocket p2p port on: %d' % int(sport))
        try:
            msg = {'nomessageflag':'0'}
            await self.init_connection(ws,msg)
        except (ConnectionClosed):
            print('connection_closed '+str(sport))



    async def connect_to_peers(self, newPeers):
        # 尝试建立连接
        tasks=[]
        for peer in newPeers:
            logger.info(peer)

            try:
                print("********************************************************************开始连接peers")
                ws = await websockets.connect(peer)
                print("连接成功peers*********************************************************************")
                msg = {'type': BANDWIDTH_COORDINATION}
                msg['bandwidth']=self.band_width_dic[peer]
                target_port=peer.split(':')[2]
                self.sockets[target_port]=ws
                msg['sport']=self.sport
                tasks.append(self.init_connection(ws,msg))
            except Exception as e:
                logger.info(str(e))
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(asyncio.wait(tasks))
        except Exception as e:
            logger.info(str(e))


    #需要重写添加websocket之后的通信消息,可以是heartbeat,
    #还需要重写init_message_handler,这是业务逻辑就在这上面用type做
    async def init_connection(self, ws,message):
        # 在sockerts里加入ws，发送一个json，内容是QUERY_LATEST
        # 维持一个死循环，等待信息
        if 'type' in message.keys():
            await ws.send(JSON.dumps(message))
        while True:
            await self.init_message_handler(ws)

    #需要重写
    async def init_message_handler(self, ws):
        '''
            如果收到 QUERY_lATEST ,返回最新的块
            如果收到 QUERY_ALL ,返回所有的块
            如果收到 RESPONSE_BLOCKCHAIN ,进入到  处理信息函数（handle_blockchain_response）
        '''
        data = await ws.recv()
        message = JSON.loads(data)
        logger.info('Received message: {}'.format(data))

        await {
            QUERY_LATEST: self.send_latest_msg,
            QUERY_ALL: self.send_chain_msg,
            BANDWIDTH_COORDINATION:self.bandwidth_coordination,
            STORAGE_APPLY:self.storage_apply_handler,
            GAIN_APPLY:self.gain_apply_handler,
            SEARCH_FOR_FILE:self.search_for_file_handler,
            PROVIDE_AGREE:self.provide_agree_handler,
            TRANSMISSION_APPLY:self.transmission_apply_handler
        }[message["type"]](ws, message)


    async def send_latest_msg(self, ws, *args):
        self.test_flag=1

    async def send_chain_msg(self, ws, *args):
        print("send_chain_msg")

    async def bandwidth_coordination(self, ws, *args):
        msg=args[0]
        target_port=msg['sport']
        target="{}:{}".format(ws.remote_address[0], target_port)
        bandwidth=int(msg['bandwidth'])
        self.sockets[target_port]=ws
        self.band_width_dic[target]=bandwidth


    async def broadcast(self, message):
        print(self.sockets.keys())
        for port in self.sockets.keys():
            logger.info(port)
            await self.sockets[port].send(JSON.dumps(message))


    async def get_all_files_local(self, request):
        result={"files":self.files}
        return json(JSON.dumps(result))

    async def search_for_file(self, request):
        files=request.json["files"]
        local_file_list=[]
        for f in self.files:
            local_file_list.append(f['hash'])
        for tf in files:
            await self.his_log(tf,"search_begin",'no_target')
            if not tf['hash'] in local_file_list:
                message = {'type': SEARCH_FOR_FILE}
                message['file']=tf
                await self.broadcast(message)
            else:
                await self.his_log(tf,'search_success','local')
        return json(JSON.dumps({'result':'success'}))

    async def save(self, request):
        files=request.json["files"]
        for file in files:
            t=round(file['size']/bwtn,2)
            self.storage_consumed=self.storage_consumed+int(file['size'])
            self.files.append(file)
            await self.his_log(file,'local_storage','no_target')
            await asyncio.sleep(t)
            await self.place_backup(file,request.json['license'])
        return json(JSON.dumps({"result": "*** Local storage completed, automatic backup started ***"}))

    async def place_backup(self, file,license):
        for targetport in license['targets']:
            if targetport in self.sockets.keys():
                ws=self.sockets[targetport]
                logger.info(ws)
                await self.his_log(file, 'back_up_begin',targetport)
                message={'type':STORAGE_APPLY}
                message['file']=file
                message['sport']=self.sport
                message['license']=license
                await ws.send(JSON.dumps(message))

    async def storage_apply_handler(self, ws, *args):
        msg = args[0]
        print('接收到了storage_apply_handler的消息')
        license=msg['license']
        file = msg["file"]
        source_port = msg['sport']
        while True:
            print('循环中循环中***')
            if self.file_exist_check(file):
                print('文件存在检查通过')
                break
            if not self.port_locked_check(source_port):
                await self.process_port_locking(source_port)
                await self.process_file_write_in(file)
                message = {'type': GAIN_APPLY}
                message['file'] = file
                message['sport']=self.sport
                message['license'] = license
                await ws.send(JSON.dumps(message))
                await self.process_storage_delay(source_port,file)
                await self.process_port_release(source_port)
                print('端口开放,文件备份完毕,开始提供备份')
                await self.place_backup(file,license)
                print('备份提供完成')
                break
            await asyncio.sleep(0.5)

    def port_locked_check(self,port):
        if port in self.locked_port:
            return True
        else:
            return False
    def file_exist_check(self,file):
        for f in self.files:
            if file['hash'] == f['hash']:
                return True

    async def process_port_locking(self,port):
        self.locked_port.append(port)
    async def process_file_write_in(self,file):
        self.files.append(file)
        self.storage_consumed=self.storage_consumed+int(file['size'])
    async def process_storage_delay(self,port,file):
        width=0
        sec_delay=0
        file_size=float(file['size'])
        for remote_address in self.band_width_dic.keys():
            if port in remote_address:
                width=int(self.band_width_dic[remote_address])
                sec_delay=file_size*1.0/width
        await asyncio.sleep(sec_delay)
    async def process_port_release(self,port):
        self.locked_port.remove(port)

    async def gain_apply_handler(self, ws, *args):
        msg = args[0]
        file = msg["file"]
        source_port = msg['sport']
        await self.process_port_locking(source_port)
        await self.process_storage_delay(source_port,file)
        await self.process_port_release(source_port)
        await self.his_log(file,'back_up_success',source_port)

    async def search_for_file_handler(self, ws, *args):
        msg = args[0]
        file = msg["file"]
        for f in self.files:
            if f['hash']==file['hash']:
                message={'type':PROVIDE_AGREE}
                message['sport']=self.sport
                message['file']=file
                await ws.send(JSON.dumps(message))

    async def provide_agree_handler(self,ws,*args):
        msg = args[0]
        file = msg["file"]
        source_port = msg['sport']
        while True:
            if self.file_exist_check(file):
                break
            if not self.port_locked_check(source_port):
                await self.process_port_locking(source_port)
                await self.process_file_write_in(file)
                message = {'type': TRANSMISSION_APPLY}
                message['file'] = file
                message['sport'] = self.sport
                await ws.send(JSON.dumps(message))
                await self.process_storage_delay(source_port,file)
                await self.his_log(file,'search_success',source_port)
                await self.process_port_release(source_port)
                break
            await asyncio.sleep(0.5)

    async def his_log(self,file,task_type,target_port):
        #task_type分四类 back_up_begin back_up_success search_begin search_success
        log={'file_hash':file['hash']}
        log['task_type']=task_type
        log['target_port']=target_port
        log['timestamp']=round(time.time()%100000,2)
        self.history.append(log)

    async def transmission_apply_handler(self, ws, *args):
        msg = args[0]
        file = msg["file"]
        source_port = msg['sport']
        await self.process_port_locking(source_port)
        await self.process_storage_delay(source_port,file)
        await self.process_port_release(source_port)


if __name__ == '__main__':
    server = Server()
    server.app.add_task(server.connect_to_peers(initialPeers))
    server.app.run(host='0.0.0.0', port=sport, debug=True)