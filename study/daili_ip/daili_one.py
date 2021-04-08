import requests
from bs4 import BeautifulSoup
import re
hed = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",

}
url='https://www.kuaidaili.com/free/'
proxy = {"http":"http://171.13.136.52:9999"}
re1=requests.get(url=url,headers=hed,proxies=proxy)
re1.encoding='GBK'
re1.encoding='utf8'
be=BeautifulSoup(re1.text,'lxml')
# print(be)
list=[]
list1=[]
a=be.find_all('td')
dic={}
list2=[]
for i in a :
    for f in i :
        list.append(str(f))
        b=r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
        c=re.findall(b,f)
        if c !=[]:
            g=c[0][0]
            list1.append(c[0][0])
        d=r'[0-9]{4}'
        e=re.findall(d,f)
        if e !=[] and e!=['2021']:
            h=e[0]
            list2.append(h)
        # print(type(g),type(h))
#         dic.update({g:h})
print(list2)