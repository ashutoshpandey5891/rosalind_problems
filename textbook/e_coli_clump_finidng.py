#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 00:15:42 2020

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


dna_seq = ''
with open('test_data/E_coli.txt') as f:
    dna_seq = f.read()
    
k = 9
l = 500
t = 3
    
def find_k_mers(dna_seq,k):
    dna_dict = {}
    for i in range(len(dna_seq) - k + 1):
        k_mer = dna_seq[i:(i+k)]
        if k_mer in dna_dict:
            dna_dict[k_mer] += 1
        else:
            dna_dict[k_mer] = 1
    return dna_dict

@time_it
def find_pattern(dna_seq,k,l,t):
    pat_list = []
    clump = dna_seq[:l]
    pat_dict = find_k_mers(clump, k)
    for pat,pat_count in pat_dict.items():
        if pat_count == t:
            pat_list.append(pat)

    for i in range(1,len(dna_seq)-l+1):
        last_pat = clump[:k]
        clump = dna_seq[i:(i+l)]
        next_pat = clump[(l-k):]
        
        pat_dict[last_pat] -= 1
        if not next_pat in pat_dict:
            pat_dict[next_pat] = 1
        else:
            pat_dict[next_pat] += 1
        if pat_dict[next_pat] == t:
            if next_pat not in pat_list:
                pat_list.append(next_pat)
    return pat_list


print(len(find_pattern(dna_seq, k, l, t)))