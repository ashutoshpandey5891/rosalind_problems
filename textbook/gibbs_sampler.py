#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 00:09:50 2020

@author: t1
"""
import random
import time
from collections import Counter
import numpy as np

def read_file(file_path):
    k,t,N,dna_strings = None,None,None,[]
    with open(file_path) as f:
        lines = f.readlines()
        k,t,N = lines[0].strip().split(' ')
        for line in lines[1:]:
            dna_strings.append(line.strip())
    return int(k),int(t),int(N),dna_strings

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

def get_random_probable_k_mer(profile_mat,dna_string,k):
    
    '''
    computes probability of every possible 
    kmer in a dna string using profile matrix and 
    returns one based on those probabilities as weights
    
    
    '''
    prob_list = []
    kmer_list = []
    n = len(dna_string)
    mapper = {'A':0,'C':1,'G':2,'T':3}
    for i in range(n-k+1):
        kmer = dna_string[i:(i+k)]
        prob = 1
        for j in range(k):
            prob *= profile_mat[mapper[kmer[j]]][j]
        kmer_list.append(kmer)
        prob_list.append(prob)
    probs_sum = sum(prob_list)
    prob_list = [prob/probs_sum for prob in prob_list]
    random_kmer = np.random.choice(kmer_list,size=1,p = prob_list)
    return random_kmer[0]
        
    

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


def gibbs_sampler(k,t,N,dna_strings):
    # intialize random motifs
    motifs = []
    for i in range(t):
        # print(dna_strings[i])
        rand_s = random.randint(0,len(dna_strings[i]) - k)
        random_motif = dna_strings[i][rand_s : (rand_s + k)]
        motifs.append(random_motif)
    best_motifs = motifs[:]
    best_score = score_motifs(best_motifs)
    # print(best_score)
    for n_iter in range(N):
        random_int = random.randint(0,t-1)
        temp_profile_mat = motifs[:random_int] + motifs[(random_int + 1):]
        profile_mat = get_profile_mat(temp_profile_mat)
        random_motif = get_random_probable_k_mer(profile_mat,dna_strings[random_int],k)
        motifs[random_int] = random_motif
        # print(motifs)
        motif_score = score_motifs(motifs)
        # print(motif_score)
        if motif_score < best_score:
            best_motifs = motifs[:]
            best_score = motif_score
    return best_motifs,best_score


def run(k,t,N,dna_strings,epochs = 50):
    best_motifs,best_score = gibbs_sampler(k, t, N, dna_strings)
    for epoch in range(epochs):
        motif,score = gibbs_sampler(k, t, N, dna_strings)
        if score < best_score:
            best_motifs = motif[:]
            best_score = score
    return best_motifs,best_score


# file_path = 'sample_data/gibbs_sampler.txt'
# file_path = 'test_data/dataset_163_4.txt'
# k,t,N,dna_strings = read_file(file_path)
# best_motifs,best_score = run(k,t,N,dna_strings)
# print('\n'.join(best_motifs))
# print(best_score)

dsor_file_path = 'actual_data/DosR.txt'
dna_seqs = []
with open(dsor_file_path) as f:
    for line in f.readlines():
        dna_seqs.append(line.strip())
    

for i in range(8,13):
    t = len(dna_seqs)
    k = i
    N = 50
    best_motifs,best_score = run(k, t, N, dna_seqs)
    print('\n'.join(best_motifs))
           