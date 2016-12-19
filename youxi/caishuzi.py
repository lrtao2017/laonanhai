#!/usr/bin/env python
#coding:utf-8

'猜数字'

import random
#import sys

guess_number = 1
play_again = 1

while True:
    guess_number = 1
    play_again = 1


    random_number = random.randint(1,100) #生成1~100的随机数
    while guess_number <= 5:
        user_number = int(raw_input("请输入一个1~100之间的数字（包含1和100）：").strip())
        if 0 <= user_number <= 100:
            if user_number > random_number:
                print 'Think smaller, you still have %s times' % (5 - guess_number)
                guess_number += 1
                continue
            elif user_number == random_number:
                print 'good, your are right!'
                play_again = 0
                break
            else :
                print 'Think bigger, you still have %s times' % (5 - guess_number)
                guess_number += 1
                continue
        else:
            print 'Please enter a number from 1~100'
            continue
    else:
        print '大笨蛋，正确答案是 ：' , random_number
        #print 'Bigger fool, the correct answer is: %s' % random_number
        play_again = 0
    
    if play_again == 0:
        play_again_y = raw_input('Do you still want to play it again (if do not want to ,input n): ')
        if play_again_y != 'n':
            continue
        else:
            #sys.exit()
            break
        
    
        
    
                
