# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 10:45:22 2017

@author: Administrator
"""

import random
import string


def get_4(chars):
    char = "".join(random.sample(chars,4))
    return char
def make_one(num):
    ch = list()
    for i in range(num):
        char = get_4(chars)
        ch.append(char)
    co = '-'.join(ch)
    code.append(co)
    
    
def make_n(count):
    for i in range(count):
        make_one(4)
    
    
if __name__ == '__main__':
    chars = string.ascii_letters +  string.digits
    
    code = list()
    make_n(200)
    print (len(code))