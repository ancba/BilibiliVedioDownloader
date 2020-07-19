import urllib.request as request
import api
import os

if __name__ == '__main__':
    bv = str(input('视频bv号：'))
    qn = int(input('视频清晰度(参考readme文档)'))
    link = api.GetVedioLink(bv, qn)[0]
    wget = 'wget --referer "http://www.bilibili.com" "' + link + '"  -O vedio.fly'
    os.system(wget)
