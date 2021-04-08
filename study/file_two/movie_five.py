import demo1.study.movie_three
import threading
import requests
import time
from demo1.study import movie_three
import os
import re
import socket
def threding_movie(url):
    """下载ts视频并保存"""
    hed = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "cookie": "HMACCOUNT_BFESS=047733F3B123839E; BAIDUID_BFESS=5FCA5036929B4B2F87D556BCB4ED77F8:FG=1"}
    # req = requests.get(url=url, headers=hed, verify=False, timeout=300)
    # a_one = movie_three.finall_movie()
    list3=[]
    a = url.split('/')
    list3.append(a)

    for i in list3:
        timea = i[-2]
        c = i[-1]
        a = r'(.*)\.ts'
        v = re.findall(a, c)[0]
        print(v)
        dirs='D://study/movie/' + timea
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        # os.makedirs('D://study/movie/' + timea)
            # a = requests.get(k, headers=hed, verify=False, timeout=300).content  # 将视频转换成2进制

        socket.setdefaulttimeout(20)  # 这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置
        sleep_download_time = 2
        time.sleep(sleep_download_time)  # 这里时间自己设定

        req = requests.get(url=url, headers=hed, verify=False, timeout=300).content

        with open('D://study/movie/%s/%s.ts' % (timea, v), 'wb+') as kk:
            print('正在下载%s'%v)
            kk.write(req)

            print('下载ok')
if __name__ == '__main__':

    a_one = movie_three.finall_movie()
    list1=[]
    loke=threading.Lock()
    for k, v in a_one.items():
        list1.append(k)
    print('-----------',list1)
    list2=[]
    for i in list1:
        print(i)
        t = threading.Thread(target=threding_movie, args=(i,))
        t.setDaemon(True)
        list2.append(t)
        # t.start()
        print('进入线程')
    in_threding=threading.current_thread()
    # for t in threading.enumerate():
    #     if t is in_threding:
    #         continue
    #     t.join()
    for a in list2:
        a.start()
    for a in list2:
        a.join()



