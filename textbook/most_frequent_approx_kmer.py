#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 01:16:56 2020

@author: t1
"""

from itertools import product
import time
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
    dna_seq = ''
    k = None
    d = None
    with open(file_path) as f:
        lines = f.readlines()
        dna_seq = lines[0].strip()
        k,d = [int(x) for x in lines[1].strip().split(' ')]
    return dna_seq,k,d


def reverse_dna(dna_seq):
    # return ''.join([DNA_Reverse[l] for l in dna_seq[::-1]])
    mapping = str.maketrans('ATCG','TAGC')
    return dna_seq.translate(mapping)[::-1]


def get_approx_matches(pattern,dna_seq,d):
    count_matches = 0
    for i in range(len(dna_seq) - len(pattern)+1):
        tmp_pattern = dna_seq[i : (i + len(pattern))]
        if hamming(pattern, tmp_pattern) <= d:
            count_matches += 1
    return count_matches

    
    

@time_it
def get_most_freq_kmer(dna_seq,k,d):
    nuces = ['A','C','G','T']
    # time1 = time.time()
    all_kmers = [''.join(ls) for ls in product(*[nuces]*k)]
    # print(f'Time to generate {len(all_kmers)} kmers : {(time.time() - time1):.6f}')
    max_count = 0
    counts_dict = {}
    # time2 = time.time()
    for i in range(len(all_kmers)):
        kmer = all_kmers[i]
        count = get_approx_matches(kmer, dna_seq, d)
        rev_count = get_approx_matches(reverse_dna(kmer), dna_seq, d)
        counts_dict[kmer] = count + rev_count
        if count+rev_count > max_count:
            max_count = count+rev_count
            
        
    # print(f'Time to get counts : {time.time() - time2}')
    res_list = [k for k,v in counts_dict.items() if v == max_count]
    
    return res_list
    
 


# file_path = 'sample_data/m_freq_app_kmer_comp.txt'
file_path = 'test_data/rosalind_ba1j.txt'
dna_seq,k,d = read_file(file_path)
res_list = get_most_freq_kmer(dna_seq, k, d)
print(' '.join(res_list))