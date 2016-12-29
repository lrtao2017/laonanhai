#!/usr/bin/env python
#coding:utf-8


'mysqL 数据库创建表'

import MySQLdb
conn = MySQLdb.connect(host = '10.3.45.199', user = 'root', passwd = '123456', db = 'test')
cur = conn.cursor()

table_name = 'user23'

recount = cur.execute('create table %s (id int(10) not null AUTO_INCREMENT, name varchar(20) not null, phone_number char(11) not null, ID_number char(18) not null, primary key (id))' % table_name)





#conn.commit()

cur.close()
conn.close()

print recount
