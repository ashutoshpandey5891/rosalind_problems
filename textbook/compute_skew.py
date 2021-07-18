#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 01:29:11 2020

@author: t1
"""

def read_file(file_path):
    dna_seq = ''
    with open(file_path) as f:
        dna_seq = f.read().strip()
    return dna_seq


def find_skew(dna_seq,start_pos = None,end_pos = None):
    '''
    function computes the skew in the given dna sequence from start pos to end pos
    start_pos -> position in dna_seq to start (default -> 0)
    end_pos -> position in dna_Seq to stop (default -> len(dna_seq))
    
    skew(i) -> the difference in cumulative number of G and C from start pos to i
    '''
    if not start_pos:
        start_pos = 0
    if not end_pos:
        end_pos = len(dna_seq)
    
    
    skew = [0]
    for i in range(start_pos,end_pos):
        a = 0
        if dna_seq[i] == 'G':
            a = 1
        elif dna_seq[i] == 'C':
            a = -1
        skew.append(skew[-1] + a)
    return skew

def get_skew_min_pos(dna_seq,start_pos=None,end_pos = None):
    '''
    returns postitions in dna seq which correspond to min value of skew (which correspond to ori)
    '''
    res_skew = find_skew(dna_seq,start_pos,end_pos)
    min_poses = []
    min_value = min(res_skew)
    for i,val in enumerate(res_skew):
        if val == min_value:
            min_poses.append(i)
    return min_poses

# dna_seq = 'GAGCCACCGCGATA'
# res_skew = find_skew(dna_seq)

# file_path = 'sample_data/min_skew.txt'
file_path = 'test_data/dataset_7_6.txt'
dna_seq = read_file(file_path)
res_skew = get_skew_min_pos(dna_seq)
print(' '.join([str(x) for x in res_skew]))