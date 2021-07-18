#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 00:27:16 2020

@author: t1
"""

from itertools import combinations,product
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
    pattern = None
    d = 0
    with open(file_path) as f:
        lines = f.readlines()
        pattern = lines[0].strip()
        d = int(lines[1].strip())
    return pattern,d

@time_it
def get_neighbours(pattern,d):
    n = len(pattern)
    nuces = ['A','C','G','T']
    all_neighbours = [pattern]
    for i in range(1,d+1):
        fill_idxs = combinations(range(n),i)
        all_fill_pats = list(product(*[nuces]*i))
        for idxs in fill_idxs:
            orig_pat = [pattern[x] for x in idxs]
            # print(orig_pat)
            for fill_pat in all_fill_pats:
                if fill_pat != orig_pat:
                    # print(fill_pat)
                    pat_copy = list(pattern)
                    for j in range(len(fill_pat)):
                        pat_copy[idxs[j]] = fill_pat[j]
                    pat_copy = ''.join(pat_copy)
                    # print(pat_copy)
                    if pat_copy not in all_neighbours:
                        all_neighbours.append(pat_copy)
                            
    return all_neighbours

# file_path = 'sample_data/neighbours.txt'
# file_path = 'sample_data/temp_data.txt'
file_path = 'test_data/rosalind_ba1n.txt'
pattern,d = read_file(file_path)
res_list = get_neighbours(pattern, d)
print('\n'.join(res_list))