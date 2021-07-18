#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 09:08:42 2021

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
    for i in range(1,seq1_len+1):
        path_mat[i,0] = path_mat[i-1,0] - indel_score
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
            match = -1
            if (str1[i-1] == str2[j-1]):
                match = 1
            m_score = path_mat[i-1,j-1] + match
            max_arg = np.array([in_score,del_score,m_score]).argmax()
            path_mat[i,j] = np.array([in_score,del_score,m_score])[max_arg]
            backtrack_mat[i,j] = max_arg
            # 0 -> insertion , 1 -> deletion , 2 -> match/mismatch
    return path_mat,backtrack_mat,path_mat[-1,-1]

def get_max_index(str1,str2,path_mat):
    seq1_len = len(str1)
    seq2_len = len(str2)
    max_score = path_mat.max()
    for i in range(seq1_len,0,-1):
        for j in range(seq2_len,0,-1):
            if path_mat[i,j] == max_score:
                return i,j


def get_backtrack(str1,str2,path_mat,backtrack_mat):
    max_score = path_mat.max()
    # i,j = get_max_index(str1, str2, path_mat)
    i,j = len(str1),len(str2)
    # print(str1,str2)
    # print(path_mat)
    # print(i,j)
    res_1 = ''
    res_2 = ''
    while (i > 0) or (j > 0):
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
    return res_1,res_2,max_score

def create_index_pairs(str1,str2):
    start_idxs = []
    end_idxs = []
    short_len = len(str2)
    start_char = str2[0]
    end_char = str2[-1]
    for i,char in enumerate(str1):
        if char == start_char:
            start_idxs.append(i)
        if len(start_idxs) > 0:
            if (char == end_char) and (i >= start_idxs[0]+0.75*short_len):
                end_idxs.append(i)
    # print(len(start_idxs),len(end_idxs))
    idx_pairs = []
    for start_idx in start_idxs:
        for end_idx in end_idxs:
            if (end_idx >= start_idx+0.75*short_len) and (end_idx <= start_idx+1.25*short_len):
                idx_pairs.append((start_idx,end_idx))
    return idx_pairs

def get_max_score_allignment(indel_score,str1,str2,idx_pairs):
    max_score = -999999999
    res1 = None
    res2 = None
    for pair in idx_pairs:
        # print(pair)
        seq1 = str1[pair[0]:(pair[1]+1)]
        # print(seq1,str2)
        path_mat,backtrack_mat,score = get_global_allignment(indel_score, seq1, str2)
        # print(score)
        if score > max_score:
            res1,res2,_ = get_backtrack(seq1, str2, path_mat, backtrack_mat)
            # print(res1,res2)
            max_score = score
    return res1,res2,max_score

@time_it
def main(str1,str2,indel_score):
    idx_pairs = create_index_pairs(str1, str2)
    # print(idx_pairs)
    # print(idx_pairs)
    res1,res2,max_score = get_max_score_allignment(indel_score, str1, str2, idx_pairs)
    return res1,res2,max_score

# file_path = 'sample_data/fitting_allignment2.txt'
file_path = 'test_data/dataset_248_5.txt'
str1,str2 = read_file(file_path)
indel_score = 1
res1,res2,max_score = main(str1,str2,indel_score)
print(int(max_score))
print(res1[::-1])
print(res2[::-1])
