import requests
from bs4 import BeautifulSoup
import re
import os
import time
# url='http://www.b2fd.com/AAyidong/AAAbf/53444-play.html?53444-0-1'
# hed={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36","cookie":"HMACCOUNT_BFESS=047733F3B123839E; BAIDUID_BFESS=5FCA5036929B4B2F87D556BCB4ED77F8:FG=1"}
# a=requests.get(url=url,headers=hed,verify=False)
# a.encoding='GBK'
# a.encoding='UTF-8'
# # print(a.text)
# bs=BeautifulSoup(a.text,'lxml')
# # print(bs)
# bs1=bs.find_all(class_='playPan')
# # print(bs1)
# print(type(str(bs1)))
# d=str(bs1)
# # print(d)
# # d='https://www.freecnmove.com/2020/04/ae51fb31/index.m3u8'
# e=r'www.freecnmove.com(.*\.m3u8)'
# f=re.findall(e,d)
# # print(f)
# g='/'.join(f)
# h = re.sub(r'\\', '', g)
# # print(h)
# j = 'http://www.freecnmove.com' + h
# print(j)
#
# with open (r'D:/study/demo1/study/file/index .m3u8') as f :
#     for a in f:
#         b=f.readlines()[-2]
#         print(b)
#         c=re.findall(r'(.*).ts',b)
#         print(int(c[0]))

a=str(int(time.time()))
b='D:\\study\movie'+a
os.makedirs('D:\\study\movie'+a)


