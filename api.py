import urllib3
import json

http = urllib3.PoolManager()

def GetVedioInfo (bv):
    fields = {'bvid':bv}
    request = http.request(method='GET',url='http://api.bilibili.com/x/web-interface/view',fields=fields)
    return json.loads(request.data.decode("utf-8"))

def GetVedioLink (bv,qn=0):
    '''
    获取视频的直链,长度
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
