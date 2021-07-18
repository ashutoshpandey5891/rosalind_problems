#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 00:04:21 2020

@author: t1
"""
import time
from distance import hamming
from itertools import product

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
    with open(file_path) as f:
        for line in f.readlines()[1:]:
            dna_seq += line
            
    return dna_seq


   
def find_skew(dna_seq,start_pos = None,end_pos = None):
    '''
    function computes the skew in the given dna sequence from start pos to end pos
    start_pos -> position in dna_seq to start (default -> 0)
    end_pos -> position in dna_Seq to stop (default -> len(dna_seq))
    
    skew(i) -> the difference in cumulative number of G and C from start pos to i
    '''
    if not start_pos:
        start_pos = 0
    if not end_pos:
        end_pos = len(dna_seq)
    
    
    skew = [0]
    for i in range(start_pos,end_pos):
        a = 0
        if dna_seq[i] == 'G':
            a = 1
        elif dna_seq[i] == 'C':
            a = -1
        skew.append(skew[-1] + a)
    return skew

@time_it
def get_skew_min_pos(dna_seq,start_pos=None,end_pos = None):
    '''
    returns postitions in dna seq which correspond to min value of skew (which correspond to ori)
    '''
    res_skew = find_skew(dna_seq,start_pos,end_pos)
    min_poses = []
    min_value = min(res_skew)
    for i,val in enumerate(res_skew):
        if val == min_value:
            min_poses.append(i)
    return min_poses

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
    
    return res_list,max_count
    
file_path = 'actual_data/Salmonella_enterica.txt'
sal_dna = read_file(file_path)
min_skew_pos = get_skew_min_pos(sal_dna)
print(min_skew_pos)
dna_seq = sal_dna[min_skew_pos[1] : (min_skew_pos[1] + 500)]
res_list,max_count = get_most_freq_kmer(dna_seq, 9, 1)
print(res_list)
print(max_count)
