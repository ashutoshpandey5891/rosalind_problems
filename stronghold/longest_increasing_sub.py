#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:07:54 2020

@author: t1
"""
import numpy as np
from operator import itemgetter
from collections import OrderedDict


def read_nums(file_path):
    with open(file_path,'r') as f:
        lines = f.readlines()
    
    pa = np.array([int(numb) for numb in lines[1].strip().split(' ')])
    n = int(lines[0].strip())
    return pa,n



def get_long_sub(pa,n,inc = True):
    # pa -> permutation numpy vector
    # n -> length of permutation
    # inc -> (incresing)
    
    tmp_dict = {}
    for i in range(n):
        # sub_array = pa[i:]
        cur_num = pa[i]
        if inc:
            cur_val = sum(pa[(i+1):] > cur_num)
        else:
            cur_val = sum(pa[(i+1):] < cur_num)
        tmp_dict[i] = cur_val
        
    # print(tmp_dict)
    # print(' ')
    # return tmp_dict
    srt_dict = OrderedDict(sorted(tmp_dict.items(),key = lambda x : x[1],reverse = True))
    idxs_list = list(srt_dict)
    # print(srt_dict)
    # print(' ')
    # print(idxs_list)
    # print(' ')
    
    long_sub = [pa[idxs_list[0]]]
    long_idxs = [idxs_list[0]]
    if inc:
        for i in range(1,len(idxs_list)):
            # print(long_sub)
            if idxs_list[i] > long_idxs[-1] and pa[idxs_list[i]] > long_sub[-1]:
                long_idxs.append(idxs_list[i])
                long_sub.append(pa[idxs_list[i]])
    else:
        for i in range(1,len(idxs_list)):
            # print(long_sub)
            if idxs_list[i] > long_idxs[-1] and pa[idxs_list[i]] < long_sub[-1]:
                long_idxs.append(idxs_list[i])
                long_sub.append(pa[idxs_list[i]])
     
    return long_sub



file_path = 'sample_data/long_subs.txt'
# file_path = 'test_data/rosalind_lgis.txt'


# pa,n = read_nums(file_path)

# print(n,len(pa))
# n = len(pa)
# pa = np.array([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
# n = len(pa)
# tmp_dict = get_long_sub(pa, n)

pa = np.random.permutation(np.arange(10))
n = len(pa)

print(pa,n)
print(' ')
long_inc_sub = get_long_sub(pa, n)
print(' '.join([str(numb) for numb in long_inc_sub]))

long_dec_sub = get_long_sub(pa, n,inc = False)
print(' '.join([str(numb) for numb in long_dec_sub]))

# print(len(long_dec_sub),len(long_inc_sub))


# n = 5
# perm = '5 1 4 2 3'
# pa = np.array([int(p) for p in perm.split(' ')])
# tmp_dict = {}
# for i in range(n):
#     sub_array = pa[i:]
#     cur_num = pa[i]
#     cur_val = sum(sub_array < cur_num)
#     tmp_dict[i] = cur_val
    
# srt_dict = OrderedDict(sorted(tmp_dict.items(),key = lambda x : x[1],reverse = True))
# idxs_list = list(srt_dict.keys())
# dec_sub = [pa[idxs_list[0]]]
# for i in range(1,len(idxs_list)):
#     if idxs_list[i] > idxs_list[i-1] and pa[idxs_list[i]] < dec_sub[-1]:
#         dec_sub.append(pa[idxs_list[i]])

# print(dec_sub)    

# tmp_dict = {}
# for i in range(n):
#     sub_array = pa[i:]
#     cur_num = pa[i]
#     cur_val = sum(sub_array > cur_num)
#     tmp_dict[i] = cur_val
    

# srt_dict = OrderedDict(sorted(tmp_dict.items(),key = lambda x : x[1],reverse = True))
# idxs_list = list(srt_dict.keys())
# dec_sub = [pa[idxs_list[0]]]
# idxs_added = [idxs_list[0]]
# for i in range(1,len(idxs_list)):
#     if idxs_list[i] > idxs_added[-1] and pa[idxs_list[i]] > dec_sub[-1]:
#         dec_sub.append(pa[idxs_list[i]])
#         idxs_added.append(idxs_list[i])
        
# print(dec_sub)