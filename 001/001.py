# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 10:45:22 2017

@author: Administrator
"""
import pymongo
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
    co = {'code':co}
    auth.insert_one(co)
    code.append(co)
    
    
def make_n(count):
    for i in range(count):
        make_one(4)
    
    
if __name__ == '__main__':
    chars = string.ascii_letters +  string.digits
    con = pymongo.MongoClient('localhost',27017)#打开数据库端
    db = con.code   #这里建立一个库,怎样直接在已有库下面建表还未解决
    auth = db.auth
    code = list()
    make_n(200)
    print (len(code))