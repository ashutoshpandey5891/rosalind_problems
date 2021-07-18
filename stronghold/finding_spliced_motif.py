#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 10:51:24 2020

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

def get_motif_indices(motif,chrome):
    indices = []
    cur_max = 0
    for m in motif:
        idx = chrome.find(m)
        
        indices.append(cur_max + idx + 1)
        chrome = chrome[idx+1:]
        cur_max += idx+1
    return indices

# file_path = 'sample_data/find_spliced_motif.txt'
file_path = 'test_data/rosalind_sseq.txt'
dna_dict = read_fasta(file_path)
dna_seqs = list(dna_dict.values())
dna_seqs.sort(key = lambda x : len(x))
motif = dna_seqs[0]
chrome = dna_seqs[1]
ans = get_motif_indices(motif, chrome)
print(' '.join([str(i) for i in ans]))
