import requests
from bs4 import BeautifulSoup
import re
import os
import time
import random
def url_3mu8():
    url = 'http://www.b2fd.com/AAyidong/AAAbf/52745-play.html?52745-0-1'
    hed = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "cookie": "HMACCOUNT_BFESS=047733F3B123839E; BAIDUID_BFESS=5FCA5036929B4B2F87D556BCB4ED77F8:FG=1"}
    a = requests.get(url=url, headers=hed, verify=False)
    a.encoding = 'GBK'
    a.encoding = 'UTF-8'
    # print(a.text)
    bs = BeautifulSoup(a.text, 'lxml')
    # print(bs)
    bs1 = bs.find_all(class_='playPan')
    # print(bs1)
    print(type(str(bs1)))
    d = str(bs1)
    # print(d)
    # d='https://www.freecnmove.com/2020/04/ae51fb31/index.m3u8'
    e = r'www.freecnmove.com(.*\.m3u8)'
    f = re.findall(e, d)
    print(f)
    g = '/'.join(f)
    print(g)
    h = re.sub(r'\\', '', g)
    print(h)
    j='http://www.freecnmove.com'+h
    # i='0003.ts'
    # k=re.sub(r'index.m3u8',i,j)
    # print(j,k)
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
    a = str(int(time.time()))
    b = 'D://study/movie' + a
    os.makedirs('D://study/movie' )
    return b
# def add_ts():
#
#     tsPath='D://study/movie/'
#     path_list = os.listdir(tsPath)
#
#     #对文件进行排序并将排序后的ts文件路径放入列表中
#     path_list.sort()
#     li = [os.path.join(tsPath,filename) for filename in path_list]
#     #将ts路径并合成一个字符参数
#     tsfiles = '|'.join(li)
#
#     #print(tsfiles)
#
#     #指定输出文件名称
#     saveMp4file = tsPath + 'target.mp4'
#
#     #调取系统命令使用ffmpeg将ts合成mp4文件
#     cmd = 'ffmpeg -i "concat:%s" -acodec copy -vcodec copy -absf aac_adtstoasc %s'%    (tsfiles,saveMp4file)
#     os.system(cmd)

def heBingTsVideo(download_path, hebing_path):

        all_ts = os.listdir(download_path)#"合并ts文件"
        # heBingTsVideo(r'D://study/movie/', r'D://study/movie/123456.mp4')

        with open(hebing_path, 'wb+') as f:
            for i in range(len(all_ts)):
                ts_video_path = os.path.join(download_path, all_ts[i])
                f.write(open(ts_video_path, 'rb').read())
        print("合并完成！！")


if __name__ == '__main__':
    a=url_3mu8()#获取m3u8的url
    ip="%s.%s.%s.%s" % (
    random.randrange(1, 200, 20), random.randrange(1, 200, 20), random.randrange(1, 200, 20),
    random.randrange(1, 200, 20))

    hed = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                      "X-Forwarded-For": ip
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
        a=requests.get(i,headers=hed, verify=False,).content#将视频转换成2进制
        with open ('D://study/movie/%s/%s.ts'%(timea,b),'wb+') as kk:
            kk.write(a)
            print('下载ok')


