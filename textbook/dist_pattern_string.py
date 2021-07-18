#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 01:27:19 2020

@author: t1
"""

from distance import hamming

def read_file(file_path):
    pattern = None
    dna_strings = []
    with open(file_path) as f:
        lines = f.readlines()
        pattern = lines[0].strip()
        for line in lines[1].strip().split(' '):
            dna_strings.append(line.strip())
    return pattern,dna_strings

def compute_min_dist(pattern,dna_seq):
    k = len(pattern)
    min_dist = k
    min_pattern = dna_seq[:k]
    for i in range(len(dna_seq)-k+1):
        temp = dna_seq[i:(i+k)]
        temp_dist = hamming(pattern,temp)
        if temp_dist < min_dist:
            min_dist = temp_dist
            min_pattern = temp
    return min_dist,min_pattern

def compute_d(pattern,dna_strs):
    min_dist = 0
    for dna_seq in dna_strs:
        dist,temp = compute_min_dist(pattern, dna_seq)
        # print(temp)
        min_dist += dist
    return min_dist
    
# file_path = 'sample_data/dist_pattern_string.txt'
file_path = 'test_data/dataset_5164_1.txt'
pattern,dna_strings = read_file(file_path)
min_dist = compute_d(pattern,dna_strings)
print(min_dist)