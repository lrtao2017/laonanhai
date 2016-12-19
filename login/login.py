#!/usr/bin/env python
#--*-- coding=utf-8 --*--

'用户登录系统'

A_file = 'account.txt'
L_file = 'lock.txt'

Count = 0
User_Passwd = 1
Lock = 0

for i in xrange(6):
    if i >=5:
        print "用户名、密码错误五次，账号已被锁定，请联系管理员解锁账号"
        break             
           
    username = raw_input("请输入用户名：").strip()
    password = raw_input("请输入密码：").strip()
    
    
    if len(username) == 0 or len(password) == 0 :
        User_Passwd = 0
        continue
    if User_Passwd == 1:
        L = file(L_file)
        for Line in L.readlines():
            Lines = Line.split()
            #print Lines
            if username == Lines[0] :
                print "%s 账号 已经被锁定，请联系管理员解锁账号" % username
                Lock = 1
                L.close()
                break
    if Lock == 1:
        break
    else:
        login_succes = 'F'
        f = file(A_file)
        for line in f.readlines():
            lines = line.split()
            if username == lines[0] and password == lines[1]:
                print "欢迎  %s 使用数字系统" % username
                login_succes = 'T'
            if username == lines[0] and login_succes == 'F' : 
                Count += 1
        if login_succes == 'T':
            break
                
        if Count >= 5:
            l = file(L_file,'a')
            l.write(username +'\n')
            l.close()
            print "用户名、密码错误五次，账号已被锁定，请联系管理员解锁账号"
            break    
        else:
            continue