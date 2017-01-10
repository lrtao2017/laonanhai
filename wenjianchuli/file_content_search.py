#!/usr/bin/env python
#coding=utf-8

'查找文件内容差异'

file1=file('1.txt','r')
file2=file('2.txt','r')
file3=file('3.txt','a')

L_num = 0

for line1 in file1.xreadlines():
    L_num += 1
    L_exit = 0
    file2.seek(0)
    for line2 in file2.xreadlines():
        if line2.strip() == line1.strip():
            L_exit = 1
            break
    if L_exit == 0:
        file3.write('有差异的行数： %s\t' % L_num)
        file3.write(line1) 

file1.close()
file2.close()
file3.close()
