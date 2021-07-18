#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 09:37:39 2021

@author: t1
"""

import time
import numpy as np

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.clock()
        result = func(*args,**kwargs)
        end = time.clock()
        print(' {} executed in time : {:.6f} sec'.format(func.__name__,end - start))
        return result
    return wrapper

def read_file(file_path):
    str1 = None
    str2 = None
    with open(file_path) as f:
        lines = f.readlines()
        str1 = lines[0].strip()
        str2 = lines[1].strip()
    return str1,str2

def get_global_allignment(indel_score,str1,str2):
    seq1_len = len(str1)
    seq2_len = len(str2)
    path_mat = np.zeros((seq1_len+1,seq2_len+1))
    
    for j in range(1,seq2_len+1):
        path_mat[0,j] = path_mat[0,j-1] - indel_score
    backtrack_mat = np.zeros((seq1_len+1,seq2_len+1))
    backtrack_mat[1:,0] = 1
    for i in range(1,seq1_len+1):
        for j in range(1,seq2_len+1):
            # insertion  
            in_score = path_mat[i,j-1] - indel_score
            # deletion 
            del_score = path_mat[i-1,j] - indel_score
            # match/mismatch
            # letter_i_idx = letter2idx[str1[i-1]]
            # letter_j_idx = letter2idx[str2[j-1]]
            match = -2
            if (str1[i-1] == str2[j-1]):
                match = 1
            m_score = path_mat[i-1,j-1] + match
            max_arg = np.array([in_score,del_score,m_score]).argmax()
            path_mat[i,j] = np.array([in_score,del_score,m_score])[max_arg]
            backtrack_mat[i,j] = max_arg
            # 0 -> insertion , 1 -> deletion , 2 -> match/mismatch , 3 -> source
    return path_mat,backtrack_mat,path_mat[-1,:].max()


def get_max_index(str1,str2,path_mat):
    seq1_len = len(str1)
    seq2_len = len(str2)
    i = seq1_len
    j = seq2_len - np.argmax(path_mat[-1,:][::-1])
    return i,j


def get_backtrack(str1,str2,path_mat,backtrack_mat):
    
    i,j = get_max_index(str1, str2, path_mat)
    # i,j = len(str1),len(str2)
    # print(str1,str2)
    # print(path_mat)
    # print(i,j)
    res_1 = ''
    res_2 = ''
    while (i > 0) and (j > 0):
        back_val = backtrack_mat[i,j]
        if back_val == 2:
            res_1 += str1[i-1]
            res_2 += str2[j-1]
            i -= 1
            j -= 1
        elif back_val == 1:
            res_1 += str1[i-1]
            res_2 += '-'
            i -= 1
        elif back_val == 0:
            res_1 += '-'
            res_2 += str2[j-1]
            j -= 1
        # else:
        #     return res_1,res_2,max_score
    return res_1,res_2


    

# file_path = 'sample_data/overlap_allignment2.txt'
file_path = 'test_data/dataset_248_7.txt'
str1,str2 = read_file(file_path)
indel_score = 2
path_mat,back_mat,max_score = get_global_allignment(indel_score, str1, str2)
res_1,res_2 = get_backtrack(str1, str2, path_mat, back_mat)
print(int(max_score))
print(res_1[::-1])
print(res_2[::-1])