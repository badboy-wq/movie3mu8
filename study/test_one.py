import re
import os
# a='gggg mr_sdfsadgf'
# b=r'mr_\w+'
# c=re.match(b,a)
#
# print(c)
#
# a='127.0.0.1 192.168.1.66'
# b=r'([1-9]{3}(\.[0-9]{1,3}){3})'
# c=re.findall(b,a)
# print(c)
# d='https://www.freecnmove.com/2020/04/ae51fb31/index.m3u8'
# e=r'www.freecnmove.com([0-9]{3})'
# f=re.findall(e,d)
# print(f)

#视频页面vedioSRC = 'https://www.finger66.com/mobile/post/5109165?channel=wechatSession&from=singlemessage&isappinstalled=0'
#放置ts文件所在目录
# tsPath = "mp4/"
# #获取ts文件参数
# hostname = 'https://media.finger66.com'
# tsParamUrl = hostname + '/posts/84222300000/MTU1NjEwNDU0ODI2Nw==.mp4.m3u8'
# import urllib.request
# tsParamData = urllib.request.urlopen(tsParamUrl).read().decode('utf-8')
# # print(tsParamData)
# import re
# pat = '/(.*?).ts'
# tsParamArr = re.compile(pat).findall(tsParamData)
# #爬取ts文件到本地
# for n in range(0,len(tsParamArr)):
#     strArr = tsParamArr[n].split('/')
#     localTSFileName = strArr[len(strArr)-1]+'.ts'
#     tsLink = hostname + '/' + tsParamArr[n] + '.ts'
#     urllib.request.urlretrieve(tsLink, tsPath+localTSFileName )
#     # print(tsLink)
#
#
# import os
# #获取所有的ts文件
# path_list = os.listdir(tsPath)
#
# #对文件进行排序并将排序后的ts文件路径放入列表中
# path_list.sort()
# li = [os.path.join(tsPath,filename) for filename in path_list]
# #将ts路径并合成一个字符参数
# tsfiles = '|'.join(li)
#
# #print(tsfiles)
#
# #指定输出文件名称
# saveMp4file = tsPath + 'target.mp4'
#
# #调取系统命令使用ffmpeg将ts合成mp4文件
# cmd = 'ffmpeg -i "concat:%s" -acodec copy -vcodec copy -absf aac_adtstoasc %s'%    (tsfiles,saveMp4file)
# os.system(cmd)
#
# url='http://www.freecnmove.com/2020/04/644f4602/0001.ts'
# a=r'\/([0-9]{4}).ts'
# b=re.findall(a,url)
# print(b)
def add_ts():
    files = 'D://study/movie/'
    # path_list = os.listdir(tsPath)
    # print(path_list)
    # # 对文件进行排序并将排序后的ts文件路径放入列表中
    # path_list.sort()
    # li = [os.path.join(tsPath, filename) for filename in path_list]
    # # 将ts路径并合成一个字符参数
    # tsfiles = ','.join(li)
    #
    # # print(tsfiles)
    #
    # # 指定输出文件名称
    # saveMp4file = tsPath + 'target.mp4'
    #
    # # 调取系统命令使用ffmpeg将ts合成mp4文件
    # cmd = 'ffmpeg -i "concat:%s" -acodec copy -vcodec copy -absf aac_adtstoasc %s' % (tsfiles, saveMp4file)
    # os.system(cmd)
    # print('合并成功')
# def heBingTsVideo(download_path, hebing_path):
#         all_ts = os.listdir(download_path)
#
#         with open(hebing_path, 'wb+') as f:
#             for i in range(len(all_ts)):
#                 ts_video_path = os.path.join(download_path, all_ts[i])
#                 f.write(open(ts_video_path, 'rb').read())
#         print("合并完成！！")
#
#
#
# if __name__ == '__main__':
#     heBingTsVideo(r'D://study/movie/1616685874/',r'D://study/movie/11.mp4')
# list=[]
# i='http://www.freecnmove.com/2020/04/f2e9af75/0695.ts'
# a=i.split('/')
# list.append(a)
#
# for i  in list:
#     c=i[-1]
#     a=r'(.*)\.ts'
#     d=re.findall(a,c)[0]
#     print(d)
#
# with open('D://study/movie/%s' % '6666', 'w') as k:
#     k.close()

# li="""</tr>, <tr><td data-title="IP">220.249.149.93</td><td data-title="PORT">9999</td><td data-title="匿名度">高匿名</td><td data-title="类型">HTTP</td>
# <td data-title="位置">福建省南平市  联通</td>
# <td data-title="响应速度">4秒</td>
# <td data-title="最后验证时间">2021-03-30 15:31:01</td>
# </tr>, <tr>"""
#
# ls=['114.239.1.42', '9999', '高匿名', 'HTTP', '江苏省宿迁市  电信', '0.5秒', '2021-03-30 22:31:01', '171.13.136.52', '9999', '高匿名', 'HTTP', '河南省商丘市  电信', '0.5秒', '2021-03-30 21:31:01', '123.101.237.245', '9999', '高匿名', 'HTTP', '河南省商丘市  电信', '3秒', '2021-03-30 20:31:01', '49.86.57.6', '9999', '高匿名', 'HTTP', '江苏省扬州市  电信', '0.4秒', '2021-03-30 19:31:01', '49.70.89.109', '9999', '高匿名', 'HTTP', '江苏省宿迁市  电信', '0.4秒', '2021-03-30 18:31:01', '113.121.36.83', '9999', '高匿名', 'HTTP', '山东省烟台市  电信', '0.6秒', '2021-03-30 17:31:01', '182.46.84.54', '9999', '高匿名', 'HTTP', '山东省淄博市  电信', '6秒', '2021-03-30 16:31:01', '220.249.149.93', '9999', '高匿名', 'HTTP', '福建省南平市  联通', '4秒', '2021-03-30 15:31:01', '117.91.252.22', '9999', '高匿名', 'HTTP', '江苏省扬州市  电信', '0.5秒', '2021-03-30 14:31:02', '121.232.148.243', '9000', '高匿名', 'HTTP', '江苏省镇江市  电信', '0.6秒', '2021-03-30 13:31:01', '123.169.124.255', '9999', '高匿名', 'HTTP', '山东省淄博市  电信', '0.6秒', '2021-03-30 12:31:01', '123.52.97.243', '9999', '高匿名', 'HTTP', '河南省商丘市  电信', '0.5秒', '2021-03-30 11:31:01', '175.44.109.36', '9999', '高匿名', 'HTTP', '福建省南平市  联通', '0.9秒', '2021-03-30 10:31:01', '49.86.180.170', '9999', '高匿名', 'HTTP', '江苏省扬州市  电信', '3秒', '2021-03-30 09:31:01', '113.121.21.184', '9999', '高匿名', 'HTTP', '山东省烟台市  电信', '0.5秒', '2021-03-30 08:31:01']
#
# for i in ls :
#     c=re.findall(r'([1-9]{1,3}(\.[0-9]{1,3}){3})',i)
#     print(c)
# proc_random='113.233.70.88:4240'
# # pr={"http":"http//"+proc_random}
# # print(pr)

a=1
while a<100:
    a=a+1
    print(a)