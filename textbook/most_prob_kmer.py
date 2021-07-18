#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 00:28:34 2020

@author: t1
"""

def read_file(file_path):
    prob_mat = []
    k = None
    dna_seq = ''
    with open(file_path) as f:
        lines = f.readlines()
        dna_seq = lines[0].strip()
        k = int(lines[1].strip())
        for line in lines[2:]:
            probs = [0]*k
            line = line.strip().split(' ')
            for i in range(k):
                probs[i] = float(line[i])
            prob_mat.append(probs)
    return dna_seq,k,prob_mat

def get_most_prob_kmer(dna_seq,k,prob_mat):
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

# file_path = 'sample_data/most_prob_kmer.txt'
file_path = 'test_data/rosalind_ba2c.txt'
dna_seq,k,prob_mat = read_file(file_path)
# most_prob,most_kmer = get_most_prob_kmer(dna_seq, k, prob_mat)
# print(most_kmer)