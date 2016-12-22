#!/usr/bin/env python
#coding:utf-8

'替换文件中匹配的内容'

import sys,shutil,os

if len(sys.argv) <4: #获取命令行参数
    print "请使用正确方法：./file_replace.py  old_text  new_text  filename (--nobak, 不保留备份文件)"
    
else:
    old_text,new_text,file_name = sys.argv[1],sys.argv[2],sys.argv[3]
#print old_text,new_text,file_name
#备份文件
shutil.copy(file_name, '%s.bak' % file_name)
new_file = '%s.bak' % file_name

new_f = open(new_file,'rb') 
old_f = open(file_name,'wb')

for line in new_f.xreadlines(): 
    #print line
    old_f.write(line.replace(old_text,new_text)) #替换
new_f.close()
old_f.close()


if '--nobak' in  sys.argv:
    os.remove(new_file)  #删除备份文件
    
