#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 00:39:35 2020

@author: t1
"""

def read_file(file_path):
    dna_seq1 = ''
    dna_seq2 = ''
    with open(file_path) as f:
        lines = f.readlines()
        dna_seq1 = lines[0].strip()
        dna_seq2 = lines[1].strip()
        
    return dna_seq1,dna_seq2

def hamming(dna_seq1,dna_seq2):
    assert len(dna_seq1) != dna_seq2,'uneuqal lengths'
    tmp = 0
    for i in range(len(dna_seq1)):
        if dna_seq1[i] != dna_seq2[i]:
            tmp += 1
            
    return tmp


# file_path = 'sample_data/hamming.txt'
file_path = 'test_data/dataset_9_3.txt'
dna_seq1,dna_seq2 = read_file(file_path)
print(hamming(dna_seq1, dna_seq2))