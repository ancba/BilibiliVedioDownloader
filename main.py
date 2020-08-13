import api
import os

if __name__ == '__main__':
    bv = str(input('视频bv号：'))
    qn = int(input('视频清晰度(参考readme文档)'))
    link = api.GetVedioLink(bv, qn)[0]
    cookie = str(input("cookie文件存放地址(可跳过)"))
    if qn == 16 or qn == 32:
        wget = 'wget --referer "http://www.bilibili.com" "' + link + '" -O vedio.fly'
    else:
        wget = 'wget --referer "http://www.bilibili.com" --load-cookies ' + cookie + ' "' + link + '"  -O vedio.fly'
    os.system(wget)
