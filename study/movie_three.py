import requests
from bs4 import BeautifulSoup
import re
import os
import time
import random
import threading


def url_3mu8(url):
    """提取m3u8地址"""
    # url = 'http://www.b2fd.com/AAyidong/AAAbf/47205-play.html?47205-0-1'
    hed = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
        }
    try:
        a = requests.get(url=url, headers=hed, verify=False,timeout=30)
        a.encoding = 'GBK'
        a.encoding = 'UTF-8'
        # print(a.text)
        bs = BeautifulSoup(a.text, 'lxml')
        # print(bs)
        bs1 = bs.find_all(class_='playPan')
        # print(bs1)

        d = str(bs1)
        e = r'www.freecnmove.com(.*\.m3u8)'
        f = re.findall(e, d)

        g = '/'.join(f)

        h = re.sub(r'\\', '', g)
        print(h)
        j='http://www.freecnmove.com'+h
    except :
        print('提取3mu8地址超时')

        pass

    return j #返回m3u8地址

def mas_m3u8():

    # with open(r'D:/study/demo1/study/file/index .m3u8') as f:
    with open (r'D:/study/demo1/study/file_two/index .m3u8') as f:
        c=0
        list1 = []
        for a in f:
            b = f.readlines()[-2]
            print(b)
            c = re.findall(r'(.*).ts', b)
            print(int(c[0]))
            c=int(c[0]) #取文件最后一个数字
        for h in range(c + 1):
            n = "%04d" % h
            list1.append(n)
    return list1  #返回url.ts列表

def dir_movie():
    """创建movie地址"""
    a = str(int(time.time()))
    b = 'D://study/movie' + a
    os.makedirs('D://study/movie' )
    return b

def movie_url():
    """返回主页面url地址"""
    url='http://www.b2fd.com/AAyidong/AAAlb/juruboba/index-4.html'

    hed = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "cookie": "HMACCOUNT_BFESS=047733F3B123839E; BAIDUID_BFESS=5FCA5036929B4B2F87D556BCB4ED77F8:FG=1"}
    req=requests.get(url=url,headers=hed,timeout=300)
    req.encoding = 'GBK'
    req.encoding = 'UTF-8'
    be=BeautifulSoup(req.text,'lxml')
    be1=be.find_all('a')
    list=[]
    for i in be1:

        href=i.get('href')
        # print(href)
        a=r'\/[^0-9]'
        # a = r'\d*$'
        b=re.findall(a,str(href))
        print(b)
        try :
            c=b[0]
            list.append(href)
        except:
            print('没有地址')
    # print(list)
    list1=[]
    for f in list:
        a = r'\d$'
        b=re.findall(a,f)
        try:
            c=b[0]
            d='http://www.b2fd.com'+f
            list1.append(d)
        except:
            print('剔除地址')
    print(list1)
    return list1
def move_request(url):
    print(url)
    try:
        hed = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
            "cookie": "HMACCOUNT_BFESS=047733F3B123839E; BAIDUID_BFESS=5FCA5036929B4B2F87D556BCB4ED77F8:FG=1"}
        req=requests.get(url=url,headers=hed,verify=False)
        req.encoding = 'GBK'
        req.encoding = 'UTF-8'
    except :
        print('请求失败')

def finall_movie(url1):
    """下载ts
    url=主页面url
    """
    url1 = movie_url()
    list = []
    dic = {}
    for i in url1:
        a = url_3mu8(i)
        list.append(a)  # 获取m3u8地址

        hed = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",

        }
        time.sleep(1)
        try:
            b = requests.get(url=a, headers=hed, verify=False,timeout=300).content
            os.remove('D://study/demo1/study/file_two/index .m3u8')
            with open('D://study/demo1/study/file_two/index .m3u8', ('wb+')) as pp:
                pp.write(b)

            list2 = []  # 返回url列表

            for f in mas_m3u8():  # 对url进行拼接
                g = re.sub(r'index.m3u8', str(f) + '.ts', a)
                list2.append(g)
            print(list2)
            # timea = str(int(time.time()))
            # os.makedirs('D://study/movie/' + timea)
            for k in list2:
                a = r'\/([0-9]{4}).ts'
                b = re.findall(a, k)[0]  # 取最后4位数字
                dic.update({k:b})
                # a = requests.get(i, headers=hed, verify=False, timeout=300).content  # 将视频转换成2进制
                # with open('D://study/movie/%s/%s.ts' % (timea, b), 'wb+') as kk:
                #     kk.write(a)
                #     print('下载ok')
        except:
            print('提取ts超时')
        return dic

def finall_movie_two(i):
    """下载ts"""
    # url1 = movie_url()
    list = []
    dic = {}
    # for i in url1:
    a = url_3mu8(i)
    list.append(a)  # 获取m3u8地址

    hed = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",

            }
    time.sleep(1)
    b = requests.get(url=a, headers=hed, verify=False,timeout=300).content
    os.remove('D://study/demo1/study/file_two/index .m3u8')
    with open('D://study/demo1/study/file_two/index .m3u8', ('wb+')) as pp:
        pp.write(b)

    list2 = []  # 返回url列表

    for f in mas_m3u8():  # 对url进行拼接
        g = re.sub(r'index.m3u8', str(f) + '.ts', a)
        list2.append(g)
    print(list2)
            # timea = str(int(time.time()))
            # os.makedirs('D://study/movie/' + timea)
    for i in list2:
        a = r'\/([0-9]{4}).ts'
        b = re.findall(a, i)[0]  # 取最后4位数字
        dic.update({i:b})
                # a = requests.get(i, headers=hed, verify=False, timeout=300).content  # 将视频转换成2进制
                # with open('D://study/movie/%s/%s.ts' % (timea, b), 'wb+') as kk:
                #     kk.write(a)
                #     print('下载ok')

    return dic





if __name__ == '__main__':

    url1=movie_url()
    list=[]
    for i in url1:
        print(i)
        a=url_3mu8(i)
        list.append(a)#获取m3u8地址

        hed = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",

            }
        b= requests.get(url=a, headers=hed, verify=False).content
        os.remove('D://study/demo1/study/file_two/index .m3u8')
        with open ('D://study/demo1/study/file_two/index .m3u8',('wb+')) as pp:
            pp.write(b)


        list2=[]#返回url列表

        for f in mas_m3u8(): #对url进行拼接
            g=re.sub(r'index.m3u8',str(f)+'.ts',a)
            list2.append(g)
        print(list2)
        timea=str(int(time.time()))
        os.makedirs('D://study/movie/'+timea)
        for i in list2:

            a = r'\/([0-9]{4}).ts'
            b = re.findall(a, i)[0]#取最后4位数字


            a=requests.get(i,headers=hed, verify=False,timeout=300).content#将视频转换成2进制
            with open ('D://study/movie/%s/%s.ts'%(timea,b),'wb+') as kk:
                kk.write(a)
                print('下载ok')







