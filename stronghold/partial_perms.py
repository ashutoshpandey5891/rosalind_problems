#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:37:12 2020

@author: t1
"""

import time
import itertools
import numpy as np


def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.clock()
        result = func(*args,**kwargs)
        end = time.clock()
        print(' {} executed in time : {:.6f} sec'.format(func.__name__,end - start))
        return result
    return wrapper

file_path = 'sample_data/partial_perms.txt'

with open(file_path,'r') as f:
    line = f.read()
    line = line.strip().split(' ')
    n,k = int(line[0]),int(line[1])

@time_it
def get_n_perms(n,k):
    return len(list(itertools.permutations(range(1,n+1),k))) % 1000000
    # return len(list(itertools.permutations(np.arange(1,n+1),k))) % 1000000


print(get_n_perms(n, k))