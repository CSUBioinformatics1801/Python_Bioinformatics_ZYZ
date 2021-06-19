# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:17:13 2020

@author: pc
"""
#-*- coding: UTF-8 -*- 
'''
Created on 2011-3-3
@author: lihex
求自然对数的底数 e
'''
#求阶乘
def factorial(number):
    if number==1:
        return 1
    return number*factorial(number-1)
 
#根据e^x 幂级数张开式，当x=1时,n为精度参数
def sum_toE(n):
    retv=2.0
    for x in range(2,n+1):
        retv += 1/float(factorial(x))
    return retv   
        
if __name__ == '__main__':
    retv = sum_toE(10)
    print(retv)