import pymysql

conn=pymysql.connect(host='192.168.101.2',port=3306,user='root',passwd='123456',db='test',charset='utf8')

cursor = conn.cursor()

# cursor.execute('insert into class(caption) values ("式式")')  # SQL语句，class 是 mydata 库中的一个表，caption 是表中的字段。
# conn.commit()  # 确认提交
# cursor.close()  # 关闭游标
# conn.close()  # 关闭连接
r=cursor.execute("select * from student")
result=cursor.fetchall()  # 全部数据
print(result)