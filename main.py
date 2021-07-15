# script by farriq mfq
import json
import requests;
import base64;
import json
import time;
import os;
def bypass(url):
    url_byte = url.encode('utf-8')
    url_encode = base64.b64encode(url_byte)
    url_decode = url_encode.decode('utf-8')
    api = 'https://lp.nrmn.top/api/bypass?url='+url_decode
    req = requests.get(api)
    req.headers['content-type']
    'application/json; charset=utf8'
    return req.text

# intro
intro = 'Script By farriqmfq'
print(intro)
time.sleep(1)
run = 'Running script...'
print(run)
time.sleep(1)
# outro
file = open('url.txt','r')
x = file.read().split('\n')
f  = open('result.txt','w')
no  = 0
for urls in x:
    if(urls != ''):
        no+=1
        jsons = json.loads(bypass(urls))
        print('Success bypass url ke ',no)
        f.write(jsons['url']+'\n')
        if(no == len(x)):
            print('Result di file : result.txt')
    else:
        print('Url not found')
