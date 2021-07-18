#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 11:06:40 2021

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
    n,m = None,None
    down_mat = None
    right_mat = None
    with open(file_path) as f:
        lines = f.readlines()
        n,m = [int(x) for x in lines[0].strip().split(' ')]
        down_mat = np.zeros((n,m+1))
        right_mat = np.zeros((n+1,m))
        line_num = 1
        for i in range(n):
            line = lines[line_num+i]
            line_lst = line.strip().split(' ')
            for j in range(len(line_lst)):
                down_mat[i,j] = int(line_lst[j])
                
        line_num += n+1
        for i in range(n+1):
            line = lines[line_num+i]
            line_lst = line.strip().split(' ')
            for j in range(len(line_lst)):
                right_mat[i,j] = int(line_lst[j])
    return n,m,down_mat,right_mat

def get_longest_path(n,m,down_mat,right_mat):
    long_mat = np.zeros((n+1,m+1))
    for i in range(1,n+1):
        long_mat[i,0] = long_mat[i-1,0] + down_mat[i-1,0]
    
    for j in range(1,m+1):
        long_mat[0,j] = long_mat[0,j-1] + right_mat[0,j-1]
        
    for i in range(1,n+1):
        for j in range(1,m+1):
            long_mat[i,j] = max(long_mat[i-1,j]+down_mat[i-1,j],long_mat[i,j-1]+right_mat[i,j-1])
    # print(long_mat)
    return long_mat[-1,-1]


# file_path = 'sample_data/manhattan_tourist.txt'
file_path = 'test_data/dataset_261_10.txt'
n,m,down_mat,right_mat = read_file(file_path)
long_path = get_longest_path(n, m, down_mat, right_mat)
print(long_path)