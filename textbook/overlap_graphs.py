#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:57:32 2020

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
    patterns = []
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            patterns.append(line.strip())
            
    return patterns


def get_overlap(patterns):
    overlap_dict = {}
    for idx1,pattern1 in enumerate(patterns):
        for idx2,pattern2 in enumerate(patterns):
            if pattern1[1:] == pattern2[:-1]:
                if pattern1 in overlap_dict:
                    overlap_dict[pattern1].append(pattern2)
                else:
                    overlap_dict[pattern1] = [pattern2]
    return overlap_dict
        

file_path = 'sample_data/overlap_graphs.txt'
# file_path = 'test_data/dataset_198_10.txt'
# file_path = 'test_data/rosalind_ba3c.txt'
patterns = read_file(file_path)
overlap_dict = get_overlap(patterns)
for pattern,adjac_list in overlap_dict.items():
    print('{} -> {}'.format(pattern,', '.join(adjac_list)))