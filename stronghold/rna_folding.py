#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:16:01 2020

@author: t1
"""

import re
import time
import collections
import numpy as np

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


def get_perf_matchings(rna_seq):
    counts = dict(collections.Counter(rna_seq))
    counts_A = counts['A']
    counts_C = counts['C']
    
    tmp1 = 1
    tmp2 = 1
    for i in range(1,counts_A+1):
        tmp1*= i
        
    for i in range(1,counts_C+1):
        tmp2 *= i
        
    return tmp1*tmp2
    

# file_path = 'sample_data/rna_fold.txt'
file_path = 'test_data/rosalind_pmch.txt'
rna_dict = read_fasta(file_path)
rna_seq = list(rna_dict.values())[0]
print(get_perf_matchings(rna_seq))