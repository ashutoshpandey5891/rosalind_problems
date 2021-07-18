#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 02:40:47 2020

@author: t1
"""
import time
from itertools import product
from distance import hamming

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.clock()
        result = func(*args,**kwargs)
        end = time.clock()
        print(' {} executed in time : {:.6f} sec'.format(func.__name__,end - start))
        return result
    return wrapper


def read_file(file_path):
    k,d = None,None
    dna_seqs = []
    with open(file_path) as f:
        lines = f.readlines()
        k,d = lines[0].strip().split(' ')
        for line in lines[1:]:
            dna_seqs.append(line.strip())
    return int(k),int(d),dna_seqs


def get_all_kmers(k):
    nuces = ['A','C','G','T']
    all_kmers = [''.join(ls) for ls in product(*[nuces]*k)]
    return all_kmers

def pattern_in_dna1(dna_seq,pattern,d):
    n = len(pattern)
    match = False
    for i in range(len(dna_seq)-n+1):
        if hamming(dna_seq[i:(i+n)],pattern) <= d:
            match = True
            break
    return match
    

@time_it
def enumerate_motifs(dna_seqs,k,d):
    all_kmers = get_all_kmers(k)
    old_kmer_list = all_kmers.copy()
    for i in range(len(dna_seqs)):
        new_kmer_list = []
        dna_seq = dna_seqs[i]
        for kmer in old_kmer_list:
            if pattern_in_dna1(dna_seq, kmer, d):
                new_kmer_list.append(kmer)
            
        old_kmer_list = new_kmer_list
    
    return new_kmer_list
        
# file_path = 'sample_data/motif_enumer.txt'
file_path = 'test_data/rosalind_ba2a.txt'
k,d,dna_seqs = read_file(file_path)
k_mers = enumerate_motifs(dna_seqs, k, d)
print(' '.join(k_mers))

# file_path = 'actual_data/subtle_motif_dataset.txt'
# k,d,dna_seqs = read_file(file_path)
# k_mers = enumerate_motifs(dna_seqs, k, d)
# print(' '.join(k_mers))
