#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 02:46:05 2020

@author: t1
"""

def read_file(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    
    dna_seq = lines[0].strip()
    k = int(lines[1].strip())
    
    return dna_seq,k

def get_k_mer(dna_seq,k):
    dna_dict = {}
    for i in range(len(dna_seq)-k+1):
        pat = dna_seq[i:(i+k)]
        if pat in dna_dict:
            dna_dict[pat] += 1
        else:
            dna_dict[pat] = 1
            
    max_freq = max(list(dna_dict.values()))
    max_pats = []
    for key,val in dna_dict.items():
        if val == max_freq:
            max_pats.append(key)
    
    return max_pats


# file_path = 'sample_data/frequent_k_mer.txt'
file_path = 'test_data/dataset_2_10.txt'
dna_seq,k = read_file(file_path)
max_pats = get_k_mer(dna_seq, k)
print(' '.join(max_pats))