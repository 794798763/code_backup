import asyncio
import os
import websockets
import time

import json as JSON
from sanic import Sanic
from sanic.response import json
from websockets.exceptions import ConnectionClosed



class Server(object):
    def __init__(self):
        self.app = Sanic()  # 一种Python web框架
        self.flag=1
        self.app.add_route(self.tt, '/tt', methods=['GET'])
        #self.app.add_route(self.test, '/test', methods=['POST'])

    # async def func1(self):
    #     while True:
    #         print(self.flag)
    #         await asyncio.sleep(1)

    async def tt(self,requests):
        #self.flag=self.flag+1
        return json(JSON.dumps({"result": 'self.flag'}))

if __name__ == '__main__':
    server = Server()
    # server.app.add_task(server.func1())
    server.app.run(host='0.0.0.0', port=3001, debug=True)




