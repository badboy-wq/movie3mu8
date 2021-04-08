import demo1.study.movie_three
import threading
import requests
import time
from demo1.study import movie_three
import os

class Subthread(threading.Thread):
    def run(self):
        hed = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
            "cookie": "HMACCOUNT_BFESS=047733F3B123839E; BAIDUID_BFESS=5FCA5036929B4B2F87D556BCB4ED77F8:FG=1"}
        a=movie_three.finall_movie()
        list=[]
        for k,v in a.items():
            try:

                req=requests.get(url=k,headers=hed,verify=False,timeout=300)
                req.encoding = 'GBK'
                req.encoding = 'UTF-8'
                a = k.split('/')
                list.append(a)

                for i in list:
                    timea = i[-2]


                    os.makedirs('D://study/movie/' + timea)
                    a = requests.get(k, headers=hed, verify=False, timeout=300).content  # 将视频转换成2进制
                    with open('D://study/movie/%s/%s.ts' % (timea, v), 'wb+') as kk:
                        kk.write(a)
                        print('下载ok')


            except:
                print('失败')


class Subthread_two(threading.Thread):
    def run(self):
        hed = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
            "cookie": "HMACCOUNT_BFESS=047733F3B123839E; BAIDUID_BFESS=5FCA5036929B4B2F87D556BCB4ED77F8:FG=1"}

        list = []
        url1 = movie_three.movie_url()
        for i in url1:
            a = movie_three.finall_movie_two(i)
            for k, v in a.items():
                try:

                    req = requests.get(url=k, headers=hed, verify=False, timeout=300)
                    req.encoding = 'GBK'
                    req.encoding = 'UTF-8'
                    a = k.split('/')
                    list.append(a)

                    for i in list:
                        timea = i[-2]

                        os.makedirs('D://study/movie/' + timea)
                        a = requests.get(k, headers=hed, verify=False, timeout=300).content  # 将视频转换成2进制
                        with open('D://study/movie/%s/%s.ts' % (timea, v), 'wb+') as kk:
                            kk.write(a)
                            print('下载ok')


                except:
                    print('失败')

if __name__ == '__main__':
    t1=Subthread_two()
    t1.start()
    t1.join()
