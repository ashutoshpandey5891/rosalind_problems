#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 12:52:55 2021

@author: t1
"""

def read_file(file_path):
    n = None
    with open(file_path) as f:
        n = int(f.read().strip())
    return n

def get_subpeptide_count(n):
    count = 1
    for k in range(1,n+1):
        count += n-k+1
    return count

file_path = 'test_data/dataset_100_3.txt'
n = read_file(file_path)
# n=4
print(get_subpeptide_count(n))