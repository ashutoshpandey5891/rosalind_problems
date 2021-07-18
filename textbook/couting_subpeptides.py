#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:36:10 2021

@author: t1
"""

def read_file(file_path):
    n = None
    with open(file_path) as f:
        n = int(f.read().strip())
    return n

def get_circular_count(n):
    return n*(n-1)

# file_path = 'sample_data/couting_subpeptides.txt'
file_path = 'test_data/dataset_98_3.txt'
n = read_file(file_path)
print(get_circular_count(n))