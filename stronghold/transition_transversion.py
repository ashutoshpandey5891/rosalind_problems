#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:18:54 2020

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

def read_fasta(file_path):
    dna_seqs = {}
    with open(file_path,'r') as f:
        lines = f.readlines()
        cur_seq = ''
        cur_seq_name = ''
        for line in lines:
            if not line.startswith('>'):
                cur_seq += line.strip()
            else:
                if cur_seq != '' and cur_seq_name != '':
                    dna_seqs[cur_seq_name] = cur_seq
                cur_seq_name = line.replace('>','').strip()
                cur_seq = ''
        if cur_seq != '':
            dna_seqs[cur_seq_name] = cur_seq
    return dna_seqs

def get_transition_transversion_ratio(dna_seq1,dna_seq2):
    if len(dna_seq1) != len(dna_seq2):
        print('Unequal length sequences')
        return None
    transitions = 0
    transversions = 0
    for i in range(len(dna_seq1)):
        dna1 = dna_seq1[i]
        dna2 = dna_seq2[i]
        if dna1 != dna2:
            if (dna1 == 'A' and dna2 == 'G') or (dna1 == 'G' and dna2 == 'A'):
                transitions += 1
            elif (dna1 == 'C' and dna2 == 'T') or (dna1 == 'T' and dna2 == 'C'):
                transitions += 1
            else:
                transversions += 1
    print(transitions,transversions)
    return transitions/transversions
                

# file_path = 'sample_data/transition_transversion.txt'
file_path = 'test_data/rosalind_tran.txt'
dna_dict = read_fasta(file_path)
dna_seqs = list(dna_dict.values())
res = get_transition_transversion_ratio(dna_seqs[0],dna_seqs[1])
print(res)