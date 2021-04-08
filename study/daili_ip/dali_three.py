import requests
import re

def ip_daili():
    url='http://webapi.http.zhimacangku.com/getip?num=5&type=2&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
    req=requests.get(url).text
    a=r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
    c=re.findall(a,req)
    e=re.findall(r'\"port\":([0-9]{4})',req)
    print(req)
    list=[]

    for i in c:
        d=i[0]
        list.append(d)
    # for i in re :
    #     print(i)
    # print(list)
    dic=dict(zip(list,e))
    print(dic)
    return dic

if __name__ == '__main__':
    ip_daili()