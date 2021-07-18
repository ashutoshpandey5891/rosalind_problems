#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 11:56:10 2020

@author: t1
"""

import os,time


def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.clock()
        result = func(*args,**kwargs)
        end = time.clock()
        print(' {} executed in time : {:.6f} sec'.format(func.__name__,end - start))
        return result
    return wrapper


def reverse_dna(dna_seq):
    # return ''.join([DNA_Reverse[l] for l in dna_seq[::-1]])
    mapping = str.maketrans('ATCG','TAGC')
    return dna_seq.translate(mapping)[::-1]

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


def find_restriction_sites(dna_seq):
    all_sites = []
    for i in range(len(dna_seq)):
        for j in range(4,13):
            max_len = i+j
            if max_len > len(dna_seq):
                continue
            current_str = dna_seq[i : (i+j)]
            if current_str == reverse_dna(current_str):
                all_sites.append((i+1,j))
                print(i+1,j)
    return all_sites
    
    
    
# file_path = 'sample_data/restriction_sites.txt'
file_path = 'test_data/rosalind_revp.txt'
dna_dict = read_fasta(file_path)
dna_seq = list(dna_dict.values())[0]
all_sites = find_restriction_sites(dna_seq)


    
    