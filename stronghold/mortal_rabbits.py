#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 14:51:41 2020

@author: t1
"""

# temp = [1,1]
# for i in range(2,31):
#     temp.append(temp[i-1] + 2*temp[i-2])
# print(temp)
# print(temp[-1])

import numpy as np

def mortal_rabbits(n,m):
    # n -> months
    # m -> live of a rabbit
    n_rabbits = np.zeros(m,dtype='int')
    n_rabbits[0] = 1
    for i in range(2,(n+1)):
        n_rabbits_temp = np.zeros(m,dtype='int')
        n_rabbits_temp[0] = n_rabbits[1:].sum()
        for j in range(1,m):
            n_rabbits_temp[j] = n_rabbits[j-1]
        n_rabbits = n_rabbits_temp
        # print(f'n : {i}')
        # print(n_rabbits,'\n')
            
            
    popn_size = sum(n_rabbits)
    return popn_size



print('{}'.format(int(mortal_rabbits(83, 17))))
            
            