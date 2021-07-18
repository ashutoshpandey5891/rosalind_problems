#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:38:15 2021

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
    print(seq1,seq1_len)
    print(seq2,seq2_len)
    long_mat = np.zeros((seq1_len+1,seq2_len+1))
    backtrack_mat = np.zeros((seq1_len,seq2_len)) 
    for i in range()

file_path = 'sample_data/lcs_dag.txt'
seq1,seq2 = read_file(file_path)