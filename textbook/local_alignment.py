#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 09:58:57 2021

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

def read_score_mat(file_path):
    score_mat = None
    letter2idx = {}
    with open(file_path) as f:
        lines = f.readlines()
        letter_line = lines[0].strip().split()
        n = len(letter_line)
        score_mat = np.zeros((n,n))
        letter_count = 0
        for line in lines[1:]:
            line = line.strip().split()
            letter = line[0]
            assert letter == letter_line[letter_count] , "letters dont match!"
            score_mat[letter_count,:] = np.array(line[1:]).astype(int)
            letter2idx[letter] = letter_count 
            letter_count += 1
    return score_mat,letter2idx

def get_global_allignment(score_mat,letter2idx,indel_score,str1,str2):
    seq1_len = len(str1)
    seq2_len = len(str2)
    path_mat = np.zeros((seq1_len+1,seq2_len+1))
    for i in range(1,seq1_len+1):
        path_mat[i,0] = path_mat[i-1,0] - 5
    for j in range(1,seq2_len+1):
        path_mat[0,j] = path_mat[0,j-1] - 5
    backtrack_mat = np.zeros((seq1_len+1,seq2_len+1))
    backtrack_mat[1:,0] = 1
    for i in range(1,seq1_len+1):
        for j in range(1,seq2_len+1):
            # insertion  
            in_score = path_mat[i,j-1] - indel_score
            # deletion 
            del_score = path_mat[i-1,j] - indel_score
            # match/mismatch
            letter_i_idx = letter2idx[str1[i-1]]
            letter_j_idx = letter2idx[str2[j-1]]
            m_score = path_mat[i-1,j-1] + score_mat[letter_i_idx,letter_j_idx]
            max_arg = np.array([0,in_score,del_score,m_score]).argmax()
            path_mat[i,j] = np.array([0,in_score,del_score,m_score])[max_arg]
            backtrack_mat[i,j] = max_arg
            # 1 -> insertion , 2 -> deletion , 3 -> match/mismatch , 0 -> init
    return path_mat,backtrack_mat

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
    i,j = get_max_index(str1, str2, path_mat)
    res_1 = ''
    res_2 = ''
    while (i > 0) or (j > 0):
        back_val = backtrack_mat[i,j]
        if back_val == 3:
            res_1 += str1[i-1]
            res_2 += str2[j-1]
            i -= 1
            j -= 1
        elif back_val == 2:
            res_1 += str1[i-1]
            res_2 += '-'
            i -= 1
        elif back_val == 1:
            res_1 += '-'
            res_2 += str2[j-1]
            j -= 1
        else:
            return res_1,res_2,max_score
    return res_1,res_2,max_score


score_mat_file_path = 'sample_data/PAM250.txt'
# file_path = 'sample_data/local_allignment.txt'
file_path = 'test_data/dataset_247_10.txt'
score_mat,letter2idx = read_score_mat(score_mat_file_path)
str1,str2 = read_file(file_path)
indel_score = 5
path_mat,backtrack_mat = get_global_allignment(score_mat, letter2idx, indel_score, str1, str2)
res_1,res_2,max_score = get_backtrack(str1, str2, path_mat, backtrack_mat)
print(int(max_score))
print(res_1[::-1])
print(res_2[::-1])