#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:32:37 2021

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
    seq1 = None
    seq2 = None
    with open(file_path) as f:
        lines = f.readlines()

        seq1 = lines[0].strip()
        seq2 = lines[1].strip()
    return seq1,seq2

def get_lcs_backtrack(seq1,seq2):
    seq1_len = len(seq1)
    seq2_len = len(seq2)
    # print(seq1,seq1_len)
    # print(seq2,seq2_len)
    long_mat = np.zeros((seq1_len+1,seq2_len+1))
    backtrack_mat = np.zeros((seq1_len+1,seq2_len+1))
    # backtrack_mat[1:,0] = -1
    for i in range(1,seq1_len+1):
        for j in range(1,seq2_len+1):
            match = 0
            if seq1[i-1] == seq2[j-1]:
                match =1
            long_mat[i,j] = max(long_mat[i-1,j],long_mat[i,j-1],long_mat[i-1,j-1]+match) # deletion ↓ ,insertion → ,match ↘
            
            if long_mat[i,j] == long_mat[i-1,j]:
                backtrack_mat[i,j] = -1 # insertion
            elif long_mat[i,j] == long_mat[i,j-1]:#
                backtrack_mat[i,j] = 0 # deletion
            elif long_mat[i,j] == long_mat[i-1,j-1]+match:
                backtrack_mat[i,j] = 1 #match
    # print(long_mat)
    return backtrack_mat

def get_lcs(backtrack_mat,seq,i,j):
    # print(i,j)
    if i == 0 or j == 0:
        return ""
    if backtrack_mat[i,j] == 0: # deletion
        return get_lcs(backtrack_mat,seq,i,j-1)
    elif backtrack_mat[i,j] == -1: # insertion
        return get_lcs(backtrack_mat,seq,i-1,j)
    else: #match
        return get_lcs(backtrack_mat, seq, i-1, j-1) + seq[i-1]

def get_steps_count(backtrack_mat,i,j,seq1,seq2):
    steps_count = 0
    while True:
        
        print(i,j,seq1[i-1],seq2[j-1],steps_count)
        
        
        if backtrack_mat[i,j] == -1.0:
            steps_count += 1
            i -= 1
        elif backtrack_mat[i,j] == 0.0:
            steps_count += 1
            j -= 1
        else:
            if seq1[i-1] != seq2[j-1]:
                steps_count += 1
            i -= 1
            j -= 1
        
        if i == 0 or j == 0:
            return steps_count
            
    
# lcs problem    
# file_path = 'sample_data/lcs_dag.txt'
# file_path = 'test_data/dataset_245_5.txt'

#edit problem
file_path = 'sample_data/edit_problem2.txt'
# file_path = 'test_data/dataset_248_3.txt'

seq1,seq2 = read_file(file_path)
backtrack_mat = get_lcs_backtrack(seq1, seq2)
# backtrack = get_lcs(backtrack_mat,seq1,len(seq1),len(seq2))
# print(backtrack)
n_steps = get_steps_count(backtrack_mat, len(seq1),len(seq2), seq1, seq2)
print(n_steps)


            
            
            