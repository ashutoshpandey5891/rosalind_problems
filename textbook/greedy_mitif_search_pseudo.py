#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 01:08:31 2020

@author: t1
"""

import time
import os
from collections import Counter
import numpy as np
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
    k,t = None,None
    dna_strs = []
    with open(file_path) as f:
        lines = f.readlines()
        k = int(lines[0].strip().split(' ')[0])
        t = int(lines[0].strip().split(' ')[1])
        for line in lines[1:]:
            dna_strs.append(line.strip())
    return dna_strs,k,t

def get_profile_mat(dna_list):
    '''
    dna_list -> list of strings to form profile from
    returns profile matrix with pseudocounts 
    '''
    
    k = len(dna_list[0])

    dna_arr = np.array([list(x) for x in dna_list])
    # print(dna_list)
    # print(dna_arr)
    profile_mat = [[0]*k,[0]*k,[0]*k,[0]*k]
    mapper = {'A':0,'C':1,'G':2,'T':3}
    for i in range(k):
        count = dict(Counter(dna_arr[:,i]))
        # for dna,val in count.items():
        #     profile_mat[mapper[dna]][i] = (val + 1)/(2*len(dna_list))
        for dna in mapper.keys():
            if dna in count:
                profile_mat[mapper[dna]][i] = (count[dna] + 1)/(2*len(dna_list))
            else:
                profile_mat[mapper[dna]][i] = (1)/(2*len(dna_list))
    return profile_mat
        

def get_most_prob_kmer(dna_seq,k,prob_mat):
    '''
    dna_seq -> string to extract pattens from
    k -> len of pattern(k-mer)
    prob_mat -> list of lists eg -> 
    
    [[0.04, 0.24, 0.32, 0.2, 0.24, 0.24, 0.32, 0.24],
     [0.32, 0.2, 0.2, 0.36, 0.28, 0.44, 0.12, 0.28],
     [0.28, 0.36, 0.2, 0.36, 0.24, 0.24, 0.2, 0.24],
     [0.36, 0.2, 0.28, 0.08, 0.24, 0.08, 0.36, 0.24]]
    '''
    
    most_kmer = dna_seq[:k]
    most_prob = 0
    mapper = {'A':0,'C':1,'G':2,'T':3}
    for i in range(1,len(dna_seq)-k+1):
        kmer = dna_seq[i:(i+k)]
        prob = 1
        for j in range(k):
            prob *= prob_mat[mapper[kmer[j]]][j]
        if prob > most_prob:
            most_prob = prob
            most_kmer = kmer
    return most_prob,most_kmer

def score_motifs(motifs):
    k = len(motifs[0])
    t = len(motifs)
    score = 0
    concesus_str = ''
    for i in range(k):
        counts = dict(Counter([motif[i] for motif in motifs]))
        max_val = max(counts.items(),key = lambda x : x[1])
        concesus_str += max_val[0]
        score += t - max_val[1]
    return score
    
        
@time_it
def greedyMotifSearch(dna_strs,k,t):
    '''
    dna_strs -> list of dna strings
    k -> len of possible motif
    t -> # strings in dna
    '''
    best_motifs = [dna_str[:k] for dna_str in dna_strs]
    best_score = score_motifs(best_motifs)
    for i in range(0,len(dna_strs[0])-k+1):
        motifs = [dna_strs[0][i:(i+k)]]        
        for j in range(1,t):
            profile_mat = get_profile_mat(motifs)
            # print(' ')
            # print(motifs)
            # print(profile_mat)
            _,most_prob_kmer = get_most_prob_kmer(dna_strs[j],k,profile_mat)
            # print(most_prob_kmer)
            motifs.append(most_prob_kmer)
        cur_score = score_motifs(motifs)
        if cur_score < best_score:
            best_motifs = motifs
            best_score = cur_score
    return best_motifs,best_score


# file_path = 'sample_data/greedy_motif_search_pseudo.txt'
file_path = 'test_data/dataset_160_9.txt'
dna_strs,k,t = read_file(file_path)
best_motifs,_ = greedyMotifSearch(dna_strs, k, t)
for motif in best_motifs:
    print(motif)
    print('')