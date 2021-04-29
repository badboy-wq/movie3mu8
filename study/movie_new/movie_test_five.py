import requests
import re
import urllib3
import threading
import os
from study.movie_new import move_test_one
from multiprocessing import  Process,Queue
import socket
"""补充下载没有完成的ts文件最终下载方式"""

def add_move_ts(url4):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    hed = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "cookie": "HMACCOUNT_BFESS=047733F3B123839E; BAIDUID_BFESS=5FCA5036929B4B2F87D556BCB4ED77F8:FG=1"}
# with open (r'D://demo1/movie3mu8/study/file/1234.csv') as ff:
#     a=ff.readlines()
#     print(a)
#     for i in range(len(a)) :
#         if i %2==0:
#             # print(i)
#             # print(a[i])
#             fil1=a[i]
#             fil2=re.findall(r'(.*)\n',fil1)[0]
#             print(a[i+1])
#             url2=a[i+1]
#             url3=r'(.*)\n'
#             url4=re.findall(url3,url2)[0]
#             print(url4)
#             h = url2.split('/')
#             # list3.append(a)
#             #
#             # for i in list3:
#             h1=h[-1]
#
#             h2 = r'(.*)\.ts'
#             v = re.findall(h2, h1)[0]

    list3=[]
    a = url4.split('/')
    list3.append(a)

    for i in list3:
        fil2 = i[-2]
        c = i[-1]
        g = r'(.*)\.ts'
        v = re.findall(g, c)[0]
        dirs = 'D://study/movie/' + fil2
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        try:
            print('正在下载%s' % v)
            req = requests.get(url=url4, headers=hed, verify=False, timeout=6).content
            with open('D://study/movie/%s/%s.ts' % (fil2, v), 'wb+') as kk:
                    # print('正在下载%s'%v)
                kk.write(req)

                print('下载%sok'%v)
        except:

            # with open('D://demo1/movie3mu8/study/file/1234.csv', 'a+') as ff: #home
            with open('D://study/study/file/1234.csv', 'a+') as ff:  # home
                print('将超时文件写入')
                ff.write(fil2 + '\r' + url4 + '\n')
                ff.close()
            print('下载失败'+url4)
        # elif i %2!=0:
        #     print(a[i])
def add_move_ts_two(url4):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    hed = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "cookie": "HMACCOUNT_BFESS=047733F3B123839E; BAIDUID_BFESS=5FCA5036929B4B2F87D556BCB4ED77F8:FG=1"}


    list3=[]
    a = url4.split('/')
    list3.append(a)

    for i in list3:
        fil2 = i[-2]
        c = i[-1]
        g = r'(.*)\.ts'
        v = re.findall(g, c)[0]
        dirs = 'D://study/movie/' + fil2
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        try:
            print('正在下载%s' % v)
            req = requests.get(url=url4, headers=hed, verify=False, timeout=6).content
            with open('D://study/movie/%s/%s.ts' % (fil2, v), 'wb+') as kk:
                    # print('正在下载%s'%v)
                kk.write(req)

                print('下载%sok'%v)
        except requests.exceptions.ConnectionError:

            # with open('D://demo1/movie3mu8/study/file/1234.csv', 'a+') as ff: #home
            with open('D://study/study/file/1234.csv', 'a+') as ff:  # home
                print('将超时文件写入')
                ff.write(fil2 + '\r' + url4 + '\n')
                ff.close()
            print('下载失败'+url4)
        # elif i %2!=0:
        #     print(a[i])
def dizhi():
    # with open (r'D://demo1/movie3mu8/study/file/1234.csv') as ff: #home
    #     a=ff.readlines()
    with open (r'D://study/study/file/1234.csv') as ff:

        a=ff.readlines()
        print(a)
        ff.close()
    di={}
    len_list=len(a)
    for i in range(len(a)):
        if i % 2 == 0:
            # print(i)
            # print(a[i])
            fil1 = a[i]
            fil2 = re.findall(r'(.*)\n', fil1)[0]
            print(a[i + 1])
            url2 = a[i + 1]
            url3 = r'(.*)\n'
            url4 = re.findall(url3, url2)[0]
            # print(url4)
            h = url2.split('/')
            # list3.append(a)
            #
            # for i in list3:
            h1 = h[-1]

            h2 = r'(.*)\.ts'
            v = re.findall(h2, h1)[0]
            di.update({url4:fil2})

    return di,len_list
def process_one():
    try :
        os.remove(r'D://study/study/file/1234.csv')
    except:
        print('没有文件')

def final_ts():
    # l=[]
    # l2=[]
    # di,len_list=dizhi()
    # sem = threading.Semaphore(20)
    # os.remove(r'D://study/study/file/1234.csv')
    try:
        with open (r'D://study/study/file/1234.csv') as ff:

            a=ff.readlines()
            print(a)
            ff.close()

        len_list1=len(a)
        i=0
    except:

        print('没有文件')
    while len_list1>200:
        l = []
        l2 = []
        di, len_list = dizhi()
        i=i+1
        print('112233第%s'%i)

        for k, v in di.items():
            l.append(k)
        os.remove(r'D://study/study/file/1234.csv')
        for a in l:
            # sem.acquire()
            t = threading.Thread(target=add_move_ts, args=(a,))#进行补跑线程
            t.start()
            print("开始线程")
            # sem.release()
            l2.append(t)
        for b in l2:
            b.join()
            print('线程结束')
        di, len_list1 = dizhi()
        print('进程结束')


if __name__ == '__main__':

    move_test_one.paquets()
    final_ts()
    # six_heBingTsVideo()
        # timea=list3[0][-2]
        # six_heBingTsVideo(r'D://study/movie/%s'%timea, r'D://study/movie/mp4/%s.mp4'%timea)


