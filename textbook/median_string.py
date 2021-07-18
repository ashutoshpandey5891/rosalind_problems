#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:18:40 2020

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
    dna_strings = []
    k = None
    with open(file_path) as f:
        lines = f.readlines()
        k = int(lines[0].strip())
        for line in lines[1:]:
            dna_strings.append(line.strip())
            
    return dna_strings,k

def get_all_kmers(k):
    nuces = ['A','C','G','T']
    all_kmers = [''.join(kmer) for kmer in list(product(*[nuces]*k))]
    return all_kmers

def get_min_distance_pattern(dna_seq,pattern):
    k = len(pattern)
    min_dist = k
    min_dist_pattern = dna_seq[:k]
    for i in range(1,len(dna_seq) - k + 1):
        pat = dna_seq[i:(i+k)]
        dist = hamming(pattern,pat)
        if dist < min_dist:
            min_dist = dist
            min_dist_pattern = pat
    return min_dist,min_dist_pattern

@time_it
def get_median_string(dna_strings,k):
    all_kmers = get_all_kmers(k)
    kmer_dvalue = [0]*len(all_kmers)
    for i in range(len(all_kmers)):
        kmer = all_kmers[i]
        for dna in dna_strings:
            min_dist,_ = get_min_distance_pattern(dna,kmer)
            kmer_dvalue[i] += min_dist
    min_idx = kmer_dvalue.index(min(kmer_dvalue))
    min_kmer = all_kmers[min_idx]
    return min_kmer



# file_path = 'sample_data/median_string.txt'
file_path = 'test_data/rosalind_ba2b.txt'
dna_strings,k = read_file(file_path)
min_kmer = get_median_string(dna_strings, k)
print(min_kmer)
