#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 00:46:37 2020

@author: t1
"""

def read_file(file_path):
    dna_seq = ''
    pattern = ''
    d = None
    with open(file_path) as f:
        lines = f.readlines()
        pattern = lines[0].strip()
        dna_seq = lines[1].strip()
        d = int(lines[2].strip())
    return dna_seq,pattern,d
    

def hamming(dna_seq1,dna_seq2):
    assert len(dna_seq1) != dna_seq2,'uneuqal lengths'
    tmp = 0
    for i in range(len(dna_seq1)):
        if dna_seq1[i] != dna_seq2[i]:
            tmp += 1
            
    return tmp

def get_approx_match_positions(pattern,dna_seq,d):
    start_pos = []
    for i in range(len(dna_seq) - len(pattern)+1):
        tmp_pattern = dna_seq[i : (i + len(pattern))]
        if hamming(pattern, tmp_pattern) <= d:
            start_pos.append(i)
    return start_pos



# file_path = 'sample_data/approx_hamming2.txt'
# file_path = 'test_data/dataset_9_4.txt'

# file_path = 'sample_data/approx_pattern_count.txt'
# file_path = 'sample_data/temp_data.txt'
file_path = 'test_data/rosalind_ba1h.txt'
dna_seq,pattern,d = read_file(file_path)
res = get_approx_match_positions(pattern, dna_seq, d)
# print(res)
print(' '.join([str(s) for s in res]))   

# tmp_dna_seq = 'AACAAGCTGATAAACATTTAAAGAG' 
# tmp_pat = 'AAAAA'
# tmp_d = 2
# res = get_approx_match_positions(tmp_pat, tmp_dna_seq, tmp_d)
# print(len(res))