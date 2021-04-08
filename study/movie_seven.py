import demo1.study.movie_three
import threading
import requests
import time
from demo1.study import movie_three
import os
import re
import socket
from demo1.study.daili_ip import daili_two
from demo1.study.daili_ip import dali_three
import random

def movie_six_one(url):
    "提取一个地址的m3u8，返回k：.ts地址，b：地址最后4位数字"

    list = []
    dic = {}

    a = movie_three.url_3mu8(url)
    list.append(a)  # 获取m3u8地址

    hed = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",

        }
    time.sleep(1)
    try:
        b = requests.get(url=a, headers=hed, verify=False, timeout=300).content
        os.remove('D://study/demo1/study/file_two/index .m3u8')
        with open('D://study/demo1/study/file_two/index .m3u8', ('wb+')) as pp:
            pp.write(b)

        list2 = []  # 返回url列表

        for f in movie_three.mas_m3u8():  # 对url进行拼接
            g = re.sub(r'index.m3u8', str(f) + '.ts', a)
            list2.append(g)
        # print(list2)
            # timea = str(int(time.time()))
            # os.makedirs('D://study/movie/' + timea)
        for k in list2:
            a = r'\/([0-9]{4}).ts'
            b = re.findall(a, k)[0]  # 取最后4位数字
            dic.update({k: b})
                # a = requests.get(i, headers=hed, verify=False, timeout=300).content  # 将视频转换成2进制
                # with open('D://study/movie/%s/%s.ts' % (timea, b), 'wb+') as kk:
                #     kk.write(a)
                #     print('下载ok')
    except:
        print('提取ts超时')
    return dic
def six_threding_movie(url2):
    """下载ts视频并保存"""
    hed = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "cookie": "HMACCOUNT_BFESS=047733F3B123839E; BAIDUID_BFESS=5FCA5036929B4B2F87D556BCB4ED77F8:FG=1"}
    # req = requests.get(url=url, headers=hed, verify=False, timeout=300)
    # a_one = movie_three.finall_movie()
    list3=[]
    a = url2.split('/')
    list3.append(a)
    proc = {'183.165.249.155': '4245', '223.244.193.118': '4278', '114.239.218.229': '4236', '36.34.14.112': '4226', '223.243.173.179': '4278'}
    list4=[]
    for k1,v1 in proc.items():
        kv=k1+":"+v1
        list4.append(kv)
    proc_random=random.choice(list4)
    print(proc_random)
    #{'117.57.100.198': '4264', '125.79.48.220': '4278', '117.94.183.226': '4257', '125.111.146.50': '4205'}
    # ip= random.sample(proc, 1)
    for i in list3:
        timea = i[-2]
        c = i[-1]
        a = r'(.*)\.ts'
        v = re.findall(a, c)[0]
        # print(v)
        dirs='D://study/movie/' + timea
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        # os.makedirs('D://study/movie/' + timea)
            # a = requests.get(k, headers=hed, verify=False, timeout=300).content  # 将视频转换成2进制

        socket.setdefaulttimeout(20)  # 这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置
        sleep_download_time = 2
        time.sleep(sleep_download_time)  # 这里时间自己设定


        proxy = {"http": "http://171.13.136.52:9999"}
        proc_random = random.choice(list4)
        # print(proc_random)
        pr={"http":"http//"+proc_random}
        # print('1111111'+pr)
        try:

            req = requests.get(url=url2, headers=hed, proxies=pr,verify=False, timeout=60).content
            print('正在请求%s' % url2)
            with open('D://study/movie/%s/%s.ts' % (timea, v), 'wb+') as kk:
                # print('正在下载%s'%v)
                kk.write(req)

                print('下载%sok'%v)
        except :
            req = requests.get(url=url2, headers=hed, verify=False, timeout=300).content
            print('正在请求本地ip%s' % url2)
            with open('D://study/movie/%s/%s.ts' % (timea, v), 'wb+') as kk:
                # print('正在下载%s'%v)
                kk.write(req)

                print('未使用代理IP下载%sok'%v)
    # return timea

def six_heBingTsVideo(download_path, hebing_path):

    all_ts = os.listdir(download_path)  # "合并ts文件"
        # heBingTsVideo(r'D://study/movie/', r'D://study/movie/123456.mp4')

    with open(hebing_path, 'wb+') as f:
        for i in range(len(all_ts)):
            ts_video_path = os.path.join(download_path, all_ts[i])
            f.write(open(ts_video_path, 'rb').read())
    print("合并完成！！")
if __name__ == '__main__':
    list_url=movie_three.movie_url()
    for url in list_url:
        # url='http://www.b2fd.com/AAyidong/AAAbf/56030-play.html?56030-0-1'
        loke = threading.RLock()
        l=[]
        l2=[]

        for k,v in movie_six_one(url).items():
            l.append(k)
            list4 = []
            a1 = k.split('/')
            list4.append(a1)
            # proc = daili_two.IP_TEST()
            # ip = random.sample(proc, 1)

            timea = list4[0][-2]
        for a in l:
            t=threading.Thread(target=six_threding_movie,args=(a,))
            t.start()
            print("开始线程")
            l2.append(t)
        for b in l2:
            b.join()
            print('线程结束')
        # a = url.split('/')
        # list3.append(a)
        #
        #
        # timea=six_threding_movie()
        six_heBingTsVideo(r'D://study/movie/%s'%timea, r'D://study/movie/mp4/%s.mp4'%timea)


