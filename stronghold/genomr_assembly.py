#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 11:49:48 2020

@author: t1
"""
import re
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
        
def dna_seq_match(seq1,seq2):
    min_len = min(len(seq1),len(seq2))
    for i in range(int(min_len/2) + 1, min_len):
        if seq1[-i:] == seq2[:i]:
            return seq1+seq2[i:]
    return None


# @time_it
def get_short_chrome(dna_seqs):
    # returns the shortest path to a chromosome from dna sequences
    # dna_seqs -> list of dna_seqs
    print('starting 2 seqs')
    short_idxs = (0,0)
    short_len = 1000000000000000000
    short_seq = ''
    for idx1,seq1 in enumerate(dna_seqs):
        for idx2,seq2 in enumerate(dna_seqs):
            if idx1 == idx2:
                continue
            seq_match = dna_seq_match(seq1,seq2)
            if seq_match:
                if len(seq_match) < short_len:
                    short_idxs = (idx1,idx2)
                    short_seq = seq_match
                    short_len = len(seq_match)
                    
    # print(short_idxs)
    # print(short_seq)
    # print(short_len)
    i,j = short_idxs
    if i<j:
        dna_seqs = dna_seqs[:i]+dna_seqs[(i+1):j] + dna_seqs[(j+1):]
    else:
        dna_seqs = dna_seqs[:j]+dna_seqs[(j+1):i] + dna_seqs[(i+1):]
    
    full_chrome = short_seq
    print('starting multiple seqs')
    while len(dna_seqs) > 0:
        
        short_seq = ''
        short_len = 100000000000000000000
        short_idx = 0
        for idx,seq1 in enumerate(dna_seqs):
            seq_match = dna_seq_match(full_chrome,seq1)
            if seq_match:
                if len(seq_match) < short_len:
                    short_seq = seq_match
                    short_idx = idx
                    short_len = len(seq_match)
            seq_match = dna_seq_match(seq1,full_chrome)
            if seq_match:
                if len(seq_match) < short_len:
                    short_seq = seq_match
                    short_idx = idx
                    short_len = len(seq_match)
        # print(short_len)
        # print(short_seq)
        # print(short_idx)
        # print(' ')
        dna_seqs = dna_seqs[:short_idx] + dna_seqs[(short_idx+1):]
        print(len(dna_seqs))
        full_chrome = short_seq
    return full_chrome
    
# file_path = 'sample_data/genome_assembly.txt'
file_path = 'test_data/rosalind_long.txt'
dna_dict = read_fasta(file_path)
dna_seqs = list(dna_dict.values())
full_chrome = get_short_chrome(dna_seqs)
print('Full chrome : ',full_chrome)

# print(all([seq in full_chrome for seq in list(dna_dict.values())]))

# matches_len = 0
# while matches_len != 1:
#     seq_copy1 = dna_seqs.copy()
#     seq_copy2 = dna_seqs.copy()

#     seq_matches = []
#     for seq1 in seq_copy1:
#         for i in range(len(seq_copy2)):
#             seq2 = seq_copy2[i]
#             seq_match = dna_seq_match(seq1, seq2)
#             if seq_match:
#                 seq_matches.append(seq_match)
#                 seq_copy2 = seq_copy2[:i] + seq_copy2[(i+1):]
#                 break
#     dna_seqs = seq_matches
#     matches_len = len(dna_seqs)        
#     print(matches_len)

# matches_len = 0
# while matches_len != 1:
    
    
# seq_copy1 = dna_seqs.copy()
# seq_copy2 = dna_seqs.copy()
    
# short_seq_matches = []
# for seq1 in dna_seqs:
#     seq1_matches = []
#     for seq2 in dna_seqs:
#         seq_match = dna_seq_match(seq1, seq2)
#         if seq_match:
#             seq1_matches.append(seq_match)
        
#     seq1_matches.sort(key = lambda x:len(x))
#     shortest_seq = seq1_matches[0]
#     short_seq_matches.append(shortest_seq)

























