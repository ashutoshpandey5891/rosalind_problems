#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 14:25:35 2020

@author: t1
"""

def fibonacci(n):
    nums = [0,1]
    for i in range(2,n+1):
        nums.append(nums[i-1]+nums[i-2])
    return nums


# res = fibonacci(21)
# print(res,'\n',res[-1])

print(fibonacci(10))