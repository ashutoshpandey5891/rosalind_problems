#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 00:54:44 2020

@author: t1
"""

import random
from collections import Counter
import numpy as np

def read_file(file_path):
    k,t = None,None
    dna_strings = []
    with open(file_path) as f:
        lines = f.readlines()
        k = int(lines[0].strip().split(' ')[0])
        t = int(lines[0].strip().split(' ')[1])
        for line in lines[1:]:
            dna_strings.append(line.strip())
            
    return dna_strings,k,t

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
    # print(motifs)
    score = 0
    concesus_str = ''
    
    for i in range(k):
        counts = dict(Counter([motif[i] for motif in motifs]))
        max_val = max(counts.items(),key = lambda x : x[1])
        # print(max_val)
        concesus_str += max_val[0]
        score += t - max_val[1]
    return score


def randomMotifSearch(dna_strings,k,t):
    best_motifs = []
    for i in range(t):
        n = len(dna_strings[i])
        rand_st = random.randint(0,n-k)
        best_motifs.append(dna_strings[i][rand_st : (rand_st + k)])
    motifs = best_motifs.copy()
    # print([len(motif) for motif in motifs])
    best_score = score_motifs(motifs)
    while True:
        profile = get_profile_mat(motifs)
        motifs = [get_most_prob_kmer(dna_seq, k, profile)[1] for dna_seq in dna_strings]
        sc = score_motifs(motifs)
        if sc < best_score:
            # print(sc)
            best_motifs = motifs[:]
            best_score = sc
        else:
            return best_motifs,best_score
        
def run(dna_strings,k,t,epochs = 1000):
    best_motifs,best_score = randomMotifSearch(dna_strings, k, t)

    for epoch in range(epochs-1):
        motifs,score = randomMotifSearch(dna_strings, k, t)
        if score < best_score:
            # print(score)
            best_motifs = motifs
            best_score = score
    return best_motifs,best_score
        
        
    
# file_path = 'sample_data/random_motif_search.txt'
file_path = 'test_data/dataset_161_5.txt'
dna_strings,k,t = read_file(file_path)
best_motifs,best_score = run(dna_strings,k,t)
print('\n'.join(best_motifs))
print(best_score)


