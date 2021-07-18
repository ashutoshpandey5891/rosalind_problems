#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 17:39:38 2020

@author: t1
"""
import math

def read_data(file_path):
    with open(file_path,'r') as f:
        lines = f.readlines()
    dna_seq = lines[0].strip()
    probs = lines[1].strip().split(' ')
    probs = [float(prob) for prob in probs]
    return dna_seq,probs

def get_random_prob(dna_seq,gc_probs):
    rndm_str_probs = []
    for gc_prob in gc_probs:
        g_prob = gc_prob/2
        c_prob = gc_prob/2
        a_prob = (1-gc_prob)/2
        t_prob = a_prob
        
        tot_prob = 1
        for l in dna_seq:
           if l == 'A':
               tot_prob *= a_prob
           if l == 'T':
               tot_prob *= t_prob
           if l == 'C':
               tot_prob *= c_prob
           if l == 'G':
               tot_prob *= g_prob
        tot_prob = math.log10(tot_prob)
        rndm_str_probs.append(tot_prob)
    return rndm_str_probs

# file_path = 'sample_data/intro_random_strings.txt'
file_path = 'test_data/rosalind_prob.txt'
dna_seq,probs = read_data(file_path)
# print(dna_seq,probs)    
rnd_probs = get_random_prob(dna_seq, probs)
print(' '.join(['{:.3f}'.format(p) for p in rnd_probs]))