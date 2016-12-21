#!/usr/bin/env python
#coding:UTF-8

'购物清单'

import sys

shoopping = 1
cash_error = 0
user_can_buy = 0
already_buy = 0
continue_to_buy = 'y'


already_buy_goods = []



name = {'a':'Apple(a)','b':'Beef(b)','c':'Cigarette(c)','d':'Drinking(d)','p':'P9(p)',}
Existing_products = {'Apple(a)': 50, 'Beef(b)': 100, 'Cigarette(c)': 200, 'Drinking(d)': 500, 'P9(p)': 3000}
min_price = min(Existing_products[i] for i in Existing_products)   #求单价最小值
#print min_price

while shoopping == 1:
    #保证用户输入的信息正确，并不重复空输入3次
    total_cash = raw_input('请输入您的现金数量：').strip()
    users_cash = total_cash
    if len(users_cash) == 0:
        cash_error += 1
        if cash_error < 3:
            Re_enter = raw_input('您的输入有误，是否重新输入：（y or n）').strip()
        elif Re_enter == 'n' or cash_error == 3:
            #print '欢迎下次光临，再见！'
            #sys.exit()
            shoopping = 0                        
        else:
            continue
    #在现金正确的情况下，判断是否足够可以购买商品
    if len(users_cash) != 0:
        cash_error = 0
        print '现有商品信息为：'
        for k,v in  Existing_products.items():
            print '商品名称：%-15s商品价格：%-4s' % (k,v)
        if int(users_cash) < min_price :
            Re_enter_cash = raw_input('您的现金太少，是否重新输入现金数量：(y or n)')
            if Re_enter_cash == 'n':
                #print '欢迎下次光临，再见！'
                #sys.exit()
                shoopping = 0
            else:
                continue 
        #可以购买商品的情况下打印可以购买的商品的清单               
        else:
            users_cash = int(users_cash)
            while users_cash >= min_price and shoopping != 2:
                print '你现在的现金剩余为：%s' % users_cash            
                print '您可以购买的商品为：'                
                for k,v in  Existing_products.items():
                    if v <= users_cash:                                         
                        print '商品名称：%-15s商品价格：%-4s' % (k,v)
                
                if already_buy == 1 :
                    continue_to_buy = raw_input('是否继续购物（y or n）:').strip()
                    if continue_to_buy == 'n':
                        shoopping = 2  
                         
                if continue_to_buy != 'n':
                    need_to_buy_goods = raw_input('请输入您要购买的商品的名称代码，一次只能购买一件：').strip()
                    if name.has_key(need_to_buy_goods):
                        print '您已经购买：%s' % name.get(need_to_buy_goods)
                        already_buy_goods.append(name.get(need_to_buy_goods))
                        #print already_buy_goods
                        already_spent = int(Existing_products.get(name.get(need_to_buy_goods)))
                        users_cash -= already_spent
                        already_buy = 1
                    else:
                        print '您输入的商品信息有误'
                        continue

            if users_cash < min_price:
                print '你剩余的金额为：%s' % users_cash , '剩余金额已不足'
                shoopping = 2       
    
    #打印购物清单
    if shoopping == 2:
        #打印购物清单
        already_buy_goods_set = set(already_buy_goods)
        print '\n''\n'
        print '您的购物清单为：'
        print '-------------------------------'
        print '''
%-19s%-12s%-10s ''' % ('商 品 名 称','数 量','总 价')
        for goods in already_buy_goods_set:
            goods_number = already_buy_goods.count(goods)
            goods_total_cost = goods_number * Existing_products.get(goods)
            print '''
%-15s%-10s%-10s''' % (goods,goods_number,goods_total_cost)
        print '==============================='         
        print '此次共消费：%s' % (int(total_cash) - users_cash)
        print '剩余现金为：%s ' % users_cash
                
        shoopping = 0
        
        
    #退出系统    
    if shoopping == 0:
        print '-------------------------------'
        print '欢迎下次光临，再见！'
        print '\n'
        sys.exit()    
        
        
                    
            
        
        
    
        
