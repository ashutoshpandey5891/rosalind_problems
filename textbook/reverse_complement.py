#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 03:14:30 2020

@author: t1
"""

def read_file(file_path):
    with open(file_path) as f:
        dna_seq = f.read().strip()
        
    return dna_seq

def reverse_dna(dna_seq):
    # return ''.join([DNA_Reverse[l] for l in dna_seq[::-1]])
    mapping = str.maketrans('ATCG','TAGC')
    return dna_seq.translate(mapping)[::-1]


# file_path = 'sample_data/reverse_comp.txt'
file_path = 'test_data/dataset_3_2.txt'
dna_seq = read_file(file_path)
print(reverse_dna(dna_seq))