#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 03:25:46 2020

@author: t1
"""

def read_file(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    pat = lines[0].strip()
    dna_seq = lines[1].strip()
    
    return pat,dna_seq


def get_start_pos(dna_seq,pat):
    start_pos = []
    for i in range(len(dna_seq)-len(pat)+1):
        if dna_seq[i:(i+len(pat))] == pat : 
            start_pos.append(i)
    return start_pos


# file_path = 'sample_data/pattern_in_string.txt'
# file_path = 'test_data/dataset_3_5.txt'
# pat,dna_seq = read_file(file_path)

dna_seq = 'ATGACTTCGCTGTTACGCGC'
pat = 'CGC'
start_pos = get_start_pos(dna_seq, pat)
print(' '.join([str(i) for i in start_pos]))