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
def heBingTsVideo(download_path, hebing_path):
        all_ts = os.listdir(download_path)

        with open(hebing_path, 'wb+') as f:
            for i in range(len(all_ts)):
                ts_video_path = os.path.join(download_path, all_ts[i])
                f.write(open(ts_video_path, 'rb').read())
        print("合并完成！！")



if __name__ == '__main__':
    heBingTsVideo(r'D://study/movie/',r'D://study/movie/123456.mp4')