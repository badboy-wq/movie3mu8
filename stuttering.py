# L = [2, 8, 3, 5, -2, 4]
# a=len(L)
# print(a)
# ma= L[0]
# for i in L:
#     if i > ma :
#         ma=i
#
# print(ma)

s2='2018-05-11  16:25:30  iP:172.31.28.100  8080  服务程序名称：httpd'
# 按照默认的分隔符   ’空格‘(多个空格都可以)，  分割成多个字字符串
# 使用 字符串对象自带的  split方法  分割
l1=s2.split()  # 分割后  返回为 多个自字符串的  列表
# 如果  获取 分割之后的 最后一个元素
print(l1)
print(l1[-1])