#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import os
import time
import random
import json
from xml.dom.minidom import Document
base = 'https://api.bilibili.com/x/web-interface/view?'
ua = [
    'User-Agent,Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'User-Agent,Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
    'User-Agent,Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'User-Agent,Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'User-Agent,Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'User-Agent,Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124'
]  # UA信息来自http://tools.jb51.net/table/useragent，感谢！
print('BILIBILI VIDEO TOOL BASED ON API')
print('VER 5-ATNO3 BY FUNCTIONSIR')
s_ua = 'R'
s_ua = input('您想使用哪个UA？或让计算机帮你选？ R(r)=自动选择 0～5对应6个UA [R(r)/0~5]>')
if (s_ua != 'R' and s_ua != 'r'):
    s_ua = ua[int(s_ua)]
else:
    random.seed(time.time())
    s_ua = random.choice(ua)
headers = {
    "User-Agent": s_ua
}
print('[I]UA设定为[', s_ua, ']')
video = input('输入AID/BVID（AV号/BV号，务必完整如avxxx，bvxxx。）>')
tail = video[2:]
print('[I]有效部分截取完成：[', tail, ']。')
print('[I]准备请求。')
if (video[0] == 'a' or video[0] == 'A'):
    mode = 0
    print('[I]AID MODE.')
    response = requests.get(url=base+'aid='+tail, headers=headers)
    response.encoding = 'utf-8'
    print('[I]请求已发送。')
else:
    mode = 1
    print('[I]BVID MODE.')
    response = requests.get(url=base+'bvid='+tail, headers=headers)
    response.encoding = 'utf-8'
    print('[I]请求已发送。')
print('[I]收到服务器发回的内容。[\n'+response.text+'\n]')
jdata = json.loads(response.text)
bili_v_head = 'https://www.bilibili.com/video/'
print('[I]JSON解码完成。')
print('----------------------')
print('视频信息')
print('访问地址[\n'+bili_v_head+jdata['data']['bvid']+'\n'+bili_v_head+'av'+str(jdata['data']['aid']),'\n]')
print('标题[',jdata['data']['title'],']')
print('UP主[',jdata['data']['owner']['name'],']')
print('视频简介[\n'+jdata['data']['desc']+'\n]')
print('AV号[','av'+str(jdata['data']['aid']),']')
print('BV号[',jdata['data']['bvid'],']')
print('CID[',jdata['data']['cid'],']')
print('观看人数[',jdata['data']['stat']['view'],']')
print('弹幕数[',jdata['data']['stat']['danmaku'],']')
print('点赞数[',jdata['data']['stat']['like'],']')
print('硬币数[',jdata['data']['stat']['coin'],']')
print('收藏数[',jdata['data']['stat']['favorite'],']')
print('分享数[',jdata['data']['stat']['share'],']')
print('评论数[',jdata['data']['stat']['reply'],']')
print('封面图[\n'+jdata['data']['pic']+'\n]')
print('UP主基本信息（详情请用GBUPI工具）')
print('昵称[',jdata['data']['owner']['name'],']')
print('UID[',jdata['data']['owner']['mid'],']')
print('头像[\n'+jdata['data']['owner']['face']+'\n]')
#用F12工具箱可以轻松找到弹幕API需要感谢给了我寻找以提醒的【白zz】的【https://blog.csdn.net/u014788374/article/details/80367285】～
print('XML弹幕地址[','https://api.bilibili.com/x/v1/dm/list.so?oid='+str(jdata['data']['cid']),']')
out_dm = input('输出弹幕XML内容么（可能非常长且格式神奇）？Y(y)=输出 其他=取消[Y(y)/其他]>')
if (out_dm == 'Y' or out_dm == 'y'):
    response = requests.get(url='https://api.bilibili.com/x/v1/dm/list.so?oid='+str(jdata['data']['cid']), headers=headers)
    response.encoding = 'utf-8'
    print('-----------------------\n',response.text)