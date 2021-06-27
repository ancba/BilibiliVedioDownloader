import urllib3
import json
import os

http = urllib3.PoolManager()

def GetVedioInfo (bv):
    fields = {'bvid':bv}
    request = http.request(method='GET',url='http://api.bilibili.com/x/web-interface/view',fields=fields)
    return json.loads(request.data.decode("utf-8"))

def GetVedioLink (bv,qn=0):
    '''
    获取视频的直链
    '''

    info = GetVedioInfo(bv)
    cid = info['data']['cid']
    if qn == 0:
        fields = {'bvid':bv,'cid':cid}
    else:
        fields = {'bvid':bv,'cid':cid,'qn':qn}
    request = http.request(method='GET',url='http://api.bilibili.com/x/player/playurl',fields=fields)
    back = json.loads(request.data.decode("utf=8"))
    url = back['data']['durl'][0]['url']
    backup_url = back['data']['durl'][0]['backup_url'][0]
    return url,backup_url

if __name__ == "__main__":
    bv = str(input('视频bv号：'))
    qn = int(input('视频清晰度(参考readme文档)'))
    link = GetVedioLink(bv, qn)[0]
    cookie = str(input("cookie文件存放地址(可跳过)"))
    if qn == 16 or qn == 32:
        wget = 'wget --referer "http://www.bilibili.com" "' + link + '" -O vedio.fly'
    else:
        wget = 'wget --referer "http://www.bilibili.com" --load-cookies ' + cookie + ' "' + link + '"  -O vedio.fly'
    os.system(wget)
