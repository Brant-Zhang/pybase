#!/usr/bin/env python3

import http.client
import json
import time

defaultval="{\"code\":1,\"msg\":\"no record right now!\"}"

def show():
    print('========{0}'.format('nihao'))
    a=19
    b=7
    c=int(a/b)
    print(c)

def post():
    host='127.0.0.1'
    url='/v1/push'
    while (True):
        ts = int(time.time())
        conn = http.client.HTTPConnection(host,1988,timeout=300)
        payload = [
            {
                "endpoint": "step-test1234",
                "metric": "status",
                "timestamp": ts,
                "step": 30,
                "value": 1,
                "counterType": "GAUGE",
                "tags": "",
            },

            {
                "endpoint": "step-test1234",
                "metric": "tunnelon",
                "timestamp": ts,
                "step": 30,
                "value": 2,
                "counterType": "GAUGE",
                "tags": "class=tws,loc=beijing",
            },
        ]
        conn.request("POST",url,json.dumps(payload))
        r1 = conn.getresponse()
        print(r1.status,r1.reason)
        conn.close()
        time.sleep(30)

def start():
    cubes = []
    host='192.168.30.89'
    url='/api/get_device_list/'
    conn = http.client.HTTPConnection(host,8002,timeout=300)
    conn.request("GET",url)
    r1 = conn.getresponse()
    data=r1.read()
    conn.close()
    cont=json.loads(data)
    for sn in cont['content']:
        #print(sn['snList'])
        for ss in sn['snList']:
            if ss!='':
                cubes.append(ss)
    print(cubes)

if __name__ == "__main__":
    post()
    #show()
