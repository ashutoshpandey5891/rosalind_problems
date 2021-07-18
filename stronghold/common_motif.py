#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:07:09 2020

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



def get_candidates(seq,n):

    return [seq[i:(i+n)] for i in range(len(seq) - n + 1)]

@time_it
def get_common_motif(seq_dict):
    seq_list = list(seq_dict.values())
    base_seq = seq_list[0]
    N = len(base_seq)
    for n in range(N,1,-1):
        cands = get_candidates(base_seq, n)
        for cand in cands : 
            if all([cand in seq for seq in seq_list[1:]]):
                print(f'seq : {cand}')
                print(f'len : {n}')
                return cand
    return False

file_path = 'test_data/rosalind_lcsm.txt'

seq_dict = read_fasta(file_path)
get_common_motif(seq_dict)