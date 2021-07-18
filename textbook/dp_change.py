#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 12:16:35 2021

@author: t1
"""

import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.clock()
        result = func(*args,**kwargs)
        end = time.clock()
        print(' {} executed in time : {:.6f} sec'.format(func.__name__,end - start))
        return result
    return wrapper

def read_file(file_path):
    money = None
    denoms_list = None
    with open(file_path) as f:
        lines = f.readlines()
        money = int(lines[0].strip())
        denoms_list = [int(x) for x in lines[1].strip().split(',')]
    return money,denoms_list

def get_dp_change(money,coins):
    min_coin_list = [0]
    min_coin_el_list = [[]]
    max_coin = max(coins)
    del_count = 0
    for i in range(1,money+1):
        # min_count = min([min_coin_list[i-c-del_count]+1 for c in coins if i >= c])
        min_count = 999999
        min_el = None
        for coin in coins:
            if coin <= i:
                coin_count = min_coin_list[i-coin-del_count]+1
                if coin_count < min_count:
                    min_count = coin_count
                    min_el = min_coin_el_list[i-coin-del_count] + [coin]
        min_coin_list.append(min_count)
        min_coin_el_list.append(min_el)
        if len(min_coin_list) > max_coin:
            min_coin_list = min_coin_list[1:]
            min_coin_el_list = min_coin_el_list[1:]
            del_count += 1
    return min_coin_list[-1],min_coin_el_list[-1]


# file_path = 'sample_data/dp_change.txt'
file_path = 'test_data/dataset_243_10.txt'
money,coins = read_file(file_path)
min_coin_count,min_el_list = get_dp_change(money, coins)
print(min_coin_count)
print(min_el_list)