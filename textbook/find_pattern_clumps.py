#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 00:57:08 2020

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
    lines = None
    with open(file_path) as f:
        lines = f.readlines()
    dna_seq = lines[0].strip()
    k,l,t = [int(num) for num in lines[1].strip().split(' ')]
    return dna_seq,k,l,t

def find_k_mers(dna_seq,k):
    dna_dict = {}
    for i in range(len(dna_seq) - k + 1):
        k_mer = dna_seq[i:(i+k)]
        if k_mer in dna_dict:
            dna_dict[k_mer] += 1
        else:
            dna_dict[k_mer] = 1
    return dna_dict

def find_pattern(dna_seq,k,l,t):
    pat_list = []
    clump = dna_seq[:l]
    pat_dict = find_k_mers(clump, k)
    for pat,pat_count in pat_dict.items():
        if pat_count == t:
            pat_list.append(pat)

    # print(pat_dict)
    for i in range(1,len(dna_seq)-l+1):
        last_pat = clump[:k]
        clump = dna_seq[i:(i+l)]
        next_pat = clump[(l-k):]
        # if next_pat == 'TAATG':
        #     print(clump)
        #     print(pat_dict)
        #     print(i)
        pat_dict[last_pat] -= 1
        if not next_pat in pat_dict:
            pat_dict[next_pat] = 1
        else:
            pat_dict[next_pat] += 1
        if pat_dict[next_pat] == t:
            if next_pat not in pat_list:
                pat_list.append(next_pat)
            # print(clump)
    return pat_list


# file_path = 'sample_data/find_pattern_clumps.txt'
file_path = 'test_data/dataset_4_5.txt'
dna_seq,k,l,t = read_file(file_path)
pat_list = find_pattern(dna_seq,k, l, t)
print(' '.join(pat_list))
