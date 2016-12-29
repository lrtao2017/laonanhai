#!/usr/bin/env python
#coding:utf-8


'mysqL 创建数据库和表并进行简单增、删、改、查操作'

import MySQLdb

#创建数据库
'''
conn = MySQLdb.connect(host = '10.3.45.199', user = 'root', passwd = '123456')
cur = conn.cursor()

db_name = 'test1'

cur.execute('create database %s ' % db_name)

conn.commit()


cur.close()
conn.close()
'''
#对数据库进行操作

conn = MySQLdb.connect(host = '10.3.45.199', user = 'root', passwd = '123456', db = 'test')
cur = conn.cursor()



#创建表
'''
table_name = 'user3'
cur.execute('create table %s (id int(10) not null AUTO_INCREMENT,name varchar(20) not null,phone_number char(11) not null,ID_number char(18) not null,primary key (id))' % table_name)
conn.commit()


cur.close()
conn.close()
'''


#增 insert into (一次增加插入多条)
'''
sql = 'insert into user (name,phone_number,ID_number) values (%s,%s,%s)'
params = [
         ('lrtao','13722442310','130429198705236230'),
         ('lrtao1','13722442311','130429198705236231'),
         ('lrtao2','13722442312','130429198705236232')
]
recount = cur.executemany(sql,params)
conn.commit()

cur.close()
conn.close()


print recount

'''

#增 insert into (一次增加插入一条)
'''
sql = 'insert into user (name,phone_number,ID_number) values (%s,%s,%s)'
params = ('lrtao','13722442310','130429198705236230')
recount = cur.execute(sql,params)
conn.commit()


cur.close()
conn.close()

print recount
'''

#删 delete

'''
sql = 'delete from user where name = %s'
params = ('lrtao')

recount = cur.execute(sql,params)
conn.commit()


cur.close()
conn.close()

print recount

'''

#改 update
'''
sql = 'update user set name = %s where id = 7'
params = ('lrtao')

recount = cur.execute(sql,params)
conn.commit()


cur.close()
conn.close()

print recount

'''




#查 select

recount = cur.execute('select * from user')
data = cur.fetchall()
cur.close()
conn.close()

print recount
print data
