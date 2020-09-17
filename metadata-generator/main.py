import random
import time
import datetime
import json
import requests
import string

location_list=['127.0.0.1:3001','127.0.0.1:3002','127.0.0.1:3003']
while(1):
    ra = random.random()
    data_hash='0x'+''.join(random.sample('123456789abcdef', 12))
    cur_time=datetime.datetime.now()
    timestamp=cur_time.strftime('%Y-%m-%d-%H-%M-%S')
    location=random.choice(location_list)
    signature=str(hash(data_hash+timestamp+location))
    r1 = requests.post(
        url="http://127.0.0.1:3003/mineBlock",
        json={
            "data":'data:'+data_hash+','+'timestamp:'+timestamp+','+'location:'+location+','+'signature:'+signature+','
        }
    )
    print(r1.json())
    time.sleep(5)
