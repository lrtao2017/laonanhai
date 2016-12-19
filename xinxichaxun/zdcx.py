#!/usr/bin/env python
#coding:utf-8

"字典和列表应用"

import sys

contact_dic = {}
#将文件生成字典
with open("zidian.txt") as f:
    for i in f.readlines():
        line = i.strip().split() #将行转换成列表，并去掉两端的空格
        contact_dic[line[0]]=line[1:]  #生成字典
#print contact_dic

#查找信息
XZ = 0

for i in range(6):
    if i == 5:
        print "您的信息有误，请确认后再查寻"
        sys.exit()
    search = raw_input("请输入你要查找的信息：")
    if len(search.strip()) < 2:
        print "输入有误！"
        continue
    if 3 <= len(search.strip()) <= 4 and 'com' in search:
        print "请提供多余5个字符的邮箱信息"
        continue
            
    if contact_dic.has_key(search):
        print "%s 的联系方式为:" % search 
        print '邮箱：',contact_dic.get(search)[0]
        print '电话：',contact_dic.get(search)[1]
        print '住址：',contact_dic.get(search)[2]
        sys.exit()
    else:
        print '没有找到你要查询的姓名 %s ,通过模糊查询得到的信息如下：' % search
        for k,v in contact_dic.items():
            if k.count(search) != 0 :
                XZ = 1
                s_index = k.find(search)
                print k[:s_index] + "\033[32;1m%s\033[0m" % search + k[s_index + len(search):] + "的联系方式为:"
                #print "%s 的联系方式为:" % k
                print '邮箱：',contact_dic.get(k)[0]
                print '电话：',contact_dic.get(k)[1]
                print '住址：',contact_dic.get(k)[2]
                continue
            for t in v:              
                if t.count(search) != 0:
                #    continue
                #else:
                    XZ = 1
                    print "%s 的联系方式为:" % k
                    print '邮箱：',contact_dic.get(k)[0]
                    print '电话：',contact_dic.get(k)[1]
                    print '住址：',contact_dic.get(k)[2]
                    break                
        if XZ == 0 :
            print "您所查询的信息不存在，请核实信息是否正确"
        else:
            sys.exit()      
