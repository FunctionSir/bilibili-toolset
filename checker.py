#!/usr/bin/env python3
# -*- coding: utf-8 -*
import libabe
import requests
import random
import time
import json
import _thread
def do(a,b):
    random.seed(time.time())
    s_ua = random.choice(ua)
    headers = {
        "User-Agent": s_ua
    }
    response = requests.get(url=base+'aid='+str(a), headers=headers)
    response.encoding = 'utf-8'
    jdata = json.loads(response.text)
    if (jdata['code'] == 0):
        if (libabe.av2bv(a) == jdata['data']['bvid']):
            print('av'+str(a),'=',jdata['data']['bvid'])
        else:
            print('[E]ERR@av'+a+'!',libabe.av2bv(a),'!=',jdata['data']['bvid'],'!')
            p = input('[I]PRESS ENTER TO CONTINUE, PRESS CTRL+C TO STOP.')
print('BILIBILI VIDEO TOOL')
print('VER 5-ATNO3 BY FUNCTIONSIR')
print('BVENC/DEC-AUTO-API-OFFLINE-TESTER\n[W][I]CHANGE YOUR IP ADDR IF BANED BY BILIBILI.')
a = 0
base = 'https://api.bilibili.com/x/web-interface/view?'
ua = [
    'User-Agent,Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'User-Agent,Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
    'User-Agent,Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'User-Agent,Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'User-Agent,Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'User-Agent,Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124'
]  # UA信息来自http://tools.jb51.net/table/useragent，感谢！
p = input('[I]PRESS ENTER TO START, PRESS CTRL+C TO STOP.')
while(1):
    a = a+1
    _thread.start_new_thread(do,(a,a))
    time.sleep(0.8)
