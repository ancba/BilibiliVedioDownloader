import urllib.request as request
import api
import os

data = {
    "Sec-Fetch-Mode": "no-cors",
    "Cache-Control": "max-age=0",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Accept": "application/json, text/plain, */*",
    "Referer":"https://www.bilibili.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

if __name__ == '__main__':
    bv = str(input('视频bv号：'))
    link = api.GetVedioLink(bv)[0]
    wget = 'wget --referer "http://www.bilibili.com" "' + link + '"  -O vedio.fly'
    print(wget)
    os.system(wget)
