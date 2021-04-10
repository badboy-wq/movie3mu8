import requests
import re
import urllib3
"""补充下载没有完成的ts文件"""
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
hed = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
    "cookie": "HMACCOUNT_BFESS=047733F3B123839E; BAIDUID_BFESS=5FCA5036929B4B2F87D556BCB4ED77F8:FG=1"}
with open (r'D://demo1/movie3mu8/study/file/1234.csv') as ff:
    a=ff.readlines()
    print(a)
    for i in range(len(a)) :
        if i %2==0:
            # print(i)
            # print(a[i])
            fil1=a[i]
            fil2=re.findall(r'(.*)\n',fil1)[0]
            print(a[i+1])
            url2=a[i+1]
            url3=r'(.*)\n'
            url4=re.findall(url3,url2)[0]
            print(url4)
            h = url2.split('/')
            # list3.append(a)
            #
            # for i in list3:
            h1=h[-1]

            h2 = r'(.*)\.ts'
            v = re.findall(h2, h1)[0]
            try:
                req = requests.get(url=url4, headers=hed, verify=False, timeout=60).content
                with open('D://study/movie/%s/%s.ts' % (fil2, v), 'wb+') as kk:
                    # print('正在下载%s'%v)
                    kk.write(req)

                    print('下载%sok'%v)
            except :
                print('下载失败'+url4)
        # elif i %2!=0:
        #     print(a[i])




