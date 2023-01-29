#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: checkin.py(GLaDOS签到)
Author: Hennessey
Date: 2023/1/12 9:01
cron: 40 0 * * *
new Env('GLaDOS签到');
Update: 2023/1/29 更新描述信息
"""


import requests,json,os,sys,time

# 在青龙面板环境变量添加GR_COOKIE，并登录https://glados.rocks，按f12--网络获取cookie
def get_cookies():
    CookieGRs = []
    if os.environ.get("GR_COOKIE"):
        print("已获取并使用Env环境 Cookie")
        if '&' in os.environ["GR_COOKIE"]:
            CookieGRs = os.environ["GR_COOKIE"].split('&')
        elif '\n' in os.environ["GR_COOKIE"]:
            CookieGRs = os.environ["GR_COOKIE"].split('\n')
        else:
            CookieGRs = [os.environ["GR_COOKIE"]]
        # return CookieGRs
    else:
        print("未获取到正确✅格式的GlaDOS账号Cookie")
        return

    print(f"====================共{len(CookieGRs)}个GlaDOS账号Cookie=========\n")
    print(f"==================脚本执行- 北京时间(UTC+8)：{time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())}=====================\n")
    return CookieGRs


def load_send():
    global send
    cur_path = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(cur_path)
    if os.path.exists(cur_path + "/sendNotify.py"):
        try:
            from sendNotify import send
        except:
            send=False
            print("加载通知服务失败~")
    else:
        send=False
        print("加载通知服务失败~")


def checkin(e): 
    cookie = e
    checkin_url= "https://glados.rocks/api/user/checkin"
    state_url= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload={
        'token': 'glados.network'
    }
    try:
        checkin = requests.post(checkin_url,headers={
            'cookie': cookie ,
            'referer': referer,
            'origin':origin,
            'user-agent':useragent,
            'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
        state =  requests.get(state_url,headers={
            'cookie': cookie ,
            'referer': referer,
            'origin':origin,
            'user-agent':useragent})
    except Exception as e:
        print(f"签到失败，请检查网络：{e}")
    mess = checkin.json()['message']
    mail = state.json()['data']['email']
    time = state.json()['data']['leftDays']
    time = time.split('.')[0]
    return mess,time,mail

def run_checkin():
    tempcontent = tempcontents = ""
    cookies = get_cookies()
    for i in cookies:
        cookie = i
        ret,remain,email = checkin(cookie)
        content = f"账号：{email}\n签到结果：{ret}\n剩余天数：{remain}\n\n"
        tempcontent = tempcontents
        tempcontents =  tempcontent + content
    print(tempcontents)
    return tempcontents

if __name__ == '__main__':
    title = "GlaDOS签到通知"
    contents = run_checkin()
    load_send()
    send(title,contents)
