import os, queue, pycurl, random, urllib.parse, json, threading
from colorama import Fore, init
from discord_webhook import DiscordWebhook, DiscordEmbed
from time import sleep
import time
init(autoreset=True)

done = False
ping = 0
unrl_proxy = ''
found_unrl_proxy = False
i = 0
attempts = 0
rs = 0
rl = 0
known_emails = []
val_sess = []
proxy_list = []
usernames = queue.Queue()

def clear():
    os.system('cls') if os.name == 'nt' else os.system('clear')

def pingez():
        global ping
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, f'https://api2-t2.musical.ly/aweme/v1/commit/user/?app_language=en&language=en&version_code=770&app_name=musical_ly&version_name=7.7.0&device_platform=android&aid=1233')
        curl.setopt(pycurl.SSL_VERIFYPEER, 0)
        curl.setopt(pycurl.SSL_VERIFYHOST, 0)
        curl.setopt(pycurl.NOSIGNAL, 10)
        ssid = random.choice(val_sess)
        curl.setopt(pycurl.HTTPHEADER, ['Host: api2-t2.musical.ly', 'Connection: close', 'Accept-Encoding: utf-8', 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8', f'Cookie: sessionid={ssid}', 'User-Agent: com.zhiliaoapp.musically/2018071950 (Linux; U; Android 8.0.0; ar_SA; AGS-L09; Build/HUAWEIAGS-L09; Cronet/58.0.2991.0)'])
        curl.setopt(pycurl.POSTFIELDS, urllib.parse.urlencode({'unique_id': 'ff'}))
        while 1:
            curl.setopt(pycurl.PROXY, random.choice(proxy_list))
            bef = time.time()
            curl.perform_rs()
            t = time.time() - bef 
            ping = "{:.8f}s".format(float(t))

def proxy_rotate():
    global proxy_list, found_unrl_proxy, unrl_proxy
    headers = ['Host: api22-normal-c-useast1a.tiktokv.com', 'User-Agent: com.zhiliaoapp.musically/2022106050 (Linux; U; Android 7.1.2; en; Build/N2G48H;tt-ok/3.10.0.2)', f'Cookie: store-country-code=us; store-idc=maliva; passport_csrf_token_default=8c3e70f6a35fcb1605ef273917dc81fc; passport_csrf_token=8c3e70f6a35fcb1605ef273917dc81fc; d_ticket=7ae236dd5c2a5be230677528d4d1381513b7a; multi_sids=6988331077413635078%3A9b980f3cf0f2400dce9da7653560b6a0; cmpl_token=AgQQAPNSF-RPsLDFZLFaIt0_wCS5Qwqdf4vZYPwvDg; odin_tt=d76de72aeb5d84034681b0c0176df8dca80d74880b109838c7c78603dffce69f3181472a78035bba39813d355ca43fb83fa50c4617d3c2035f01f2f303f6736fb7fcdf778eecadf9a83d71e471d0b196; sid_guard=9b980f3cf0f2400dce9da7653560b6a0%7C1634672291%7C5184000%7CSat%2C+18-Dec-2021+19%3A38%3A11+GMT; uid_tt=138c9af9cccfab8d69563528b4917a78989482b49193cb69db6ef3162867be1a; uid_tt_ss=138c9af9cccfab8d69563528b4917a78989482b49193cb69db6ef3162867be1a; sid_tt={random.choice(val_sess)}; sessionid={random.choice(val_sess)}; sessionid_ss={random.choice(val_sess)}']
    curl = pycurl.Curl()
    for proxy in proxy_list:
        if found_unrl_proxy:
            proxy = unrl_proxy
        curl.setopt(pycurl.URL, 'https://api22-normal-c-useast1a.tiktokv.com/aweme/v1/unique/id/check/?unique_id=linus&iid=7020617118086039301&device_id=6504640904983365129&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=210605&version_name=21.6.5&device_platform=android&ab_version=21.6.5&ssmix=a&device_type=SM-G935F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=a0d686f54acd5e7c&manifest_version_code=2022106050&resolution=720*1280&dpi=240&update_version_code=2022106050&_rticket=1634672368196&current_region=US&app_type=normal&sys_region=US&mcc_mnc=31031&timezone_name=Asia%2FShanghai&residence=US&ts=1634672367&timezone_offset=28800&build_number=21.6.5&region=US&uoo=0&app_language=en&carrier_region=US&locale=en&op_region=US&ac2=wifi')
        curl.setopt(pycurl.SSL_VERIFYPEER, 0)
        curl.setopt(pycurl.SSL_VERIFYHOST, 0)
        curl.setopt(pycurl.HTTPHEADER, headers)
        curl.setopt(pycurl.PROXY, f"http://{proxy}")
        curl.setopt(pycurl.NOSIGNAL, 10)
        r = curl.perform_rs()
        if r == '':
            continue
        else: 
            found_unrl_proxy = True
            unrl_proxy = proxy
            return proxy

def rpsprint():
    while True:
                print(f"[{Fore.RED}>{Fore.RESET}] Ping : {ping} | Attempts : {attempts} | R/S: {rs}", end='\r')

def stats():
    global attempts, rs
    clear()
    threading.Thread(target=pingez).start()
    print(f'\t[{Fore.RED} TikTok Claimer{Fore.RESET}]\n')
    print(f'[{Fore.RED}>{Fore.RESET}] Threads : {threads}')
    print(f'[{Fore.RED}>{Fore.RESET}] Users Loaded : {usersize}')
    threading.Thread(target=rpsprint).start()
    while True:
        bef = attempts 
        sleep(1)
        rs = attempts - bef

def claimer():
        global attempts, rl, done
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, f'https://api2-t2.musical.ly/aweme/v1/commit/user/?app_language=en&language=en&version_code=770&app_name=musical_ly&version_name=7.7.0&device_platform=android&aid=1233')
        curl.setopt(pycurl.SSL_VERIFYPEER, 0)
        curl.setopt(pycurl.SSL_VERIFYHOST, 0)
        curl.setopt(pycurl.NOSIGNAL, 10)
        ssid = random.choice(val_sess)
        curl.setopt(pycurl.HTTPHEADER, ['Host: api2-t2.musical.ly', 'Connection: close', 'Accept-Encoding: utf-8', 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8', f'Cookie: sessionid={ssid}', 'User-Agent: com.zhiliaoapp.musically/2018071950 (Linux; U; Android 8.0.0; ar_SA; AGS-L09; Build/HUAWEIAGS-L09; Cronet/58.0.2991.0)'])
        try:
            while 1:
                    ssid = random.choice(val_sess)
                    user = usernames.get()
                    curl.setopt(pycurl.PROXY, random.choice(proxy_list))
                    curl.setopt(pycurl.POSTFIELDS, urllib.parse.urlencode({'unique_id': user}))
                    r = curl.perform_rs()
                    if 'unique_id' in r:
                        print(f"\n\n[{Fore.RED}>{Fore.RESET}] Claimed {user}")
                        attempts += 1
                    else:
                        usernames.put(user)
                        attempts += 1
        except: 
                pass         

clear()



print(f"[{Fore.RED}>{Fore.RESET}] Blades AutoClaimer\n")

em_pass_file = 'mails.txt' # input(f"[{Fore.RED}>{Fore.RESET}] Email File : ")
user_file = 'Targets.txt' # input(f"[{Fore.RED}>{Fore.RESET}] Username File : ")
threads = int(input(f"[{Fore.RED}>{Fore.RESET}] Threads : "))
p_file = 'Proxies.txt' # input(f"[{Fore.RED}>{Fore.RESET}] Proxy File : ")

for line in open(user_file, 'r'):
    usernames.put(line.strip())

usersize = usernames.qsize()

for line in open(p_file, 'r'):
    proxy_list.append(line.strip())

clear()

print(f"\t[{Fore.RED}Sessions{Fore.RESET}]\n")

for line in open(em_pass_file, 'r'):
    curl = pycurl.Curl()
    try:
        email, password = line.strip().split(':')
        if f"{email}:{password}" not in known_emails:
            known_emails.append(f"{email}:{password}")
            curl.setopt(pycurl.URL, f'https://api2-t2.musical.ly/passport/user/login/?iid=7027405945522603782&channel=googleplay&language=en&device_type=ART-L29&os_version=10&version_code=900&device_platform=android&aid=1233&email={email}&password={password}')
            curl.setopt(pycurl.SSL_VERIFYPEER, 0)
            curl.setopt(pycurl.SSL_VERIFYHOST, 0)
            curl.setopt(pycurl.CUSTOMREQUEST, "POST")
            curl.setopt(pycurl.HTTPHEADER, ["Host: api2-t2.musical.ly", "Connection: keep-alive", "Content-Length: 0", "Accept-Encoding: utf-8", "User-Agent: com.zhiliaoapp.musically/2018110525 (Linux; U; Android 10; en_GB; CUM PHONE V920; Build/HUAWEIART-L29; Cronet/58.0.2991.0)"])
            curl.setopt(pycurl.NOSIGNAL, 10)
            curl.setopt(pycurl.PROXY, random.choice(proxy_list))
            r = curl.perform_rs()
            if "has_password" in r:
                i += 1
                print(f"[{Fore.GREEN}Session {i}{Fore.RESET}] {json.loads(r)['data']['session_key']} ")
                val_sess.append(json.loads(r)['data']['session_key'])
            else:
                print(f"[{Fore.RED}Session Fail{Fore.RESET}] {email}:{password}")
        else:
            print(f"[{Fore.RED}Session Fail{Fore.RESET}] Used Email & Pass")
    except:
        print(f"[{Fore.GREEN}Session {Fore.RESET}] {line.strip()}")
        val_sess.append(line.strip())

sleep(1)

if len(val_sess) == 0:
    print(f"[{Fore.RED}>{Fore.RESET}] No valid sessions to continue with")
    quit(1)

threading.Thread(target=stats).start()
        
thread = [] 
for i in range(threads):
        t = threading.Thread(target=claimer)
        t.daemon = True
        t.start()
