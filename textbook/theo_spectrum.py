#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:47:58 2021

@author: t1
"""

def read_file(file_path):
    peptide = ''
    with open(file_path) as f:
        peptide = f.read().strip()
    return peptide

MOLE_MASS = {
    'G' : 57,'A':71,'S':87,'P':97,'V':99,'T':101,
    'C' : 103,'I':113,'L':113,'N':114,'D':115,'K':128,
    'Q' : 128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186
    }

def get_cyclo_spectrum(peptide):
    all_weights = [0]
    prefix_weights = [0]
    
    # get single weights and prefix
    for i in range(len(peptide)):
        w_ = MOLE_MASS[peptide[i]]
        prefix_weights.append(prefix_weights[-1]+w_)
        all_weights.append(w_)
    
    # get linear and circular subpeptide weights
    for k in range(2,len(peptide)):
        for i in range(len(peptide)):
            j = i+k
            if j > len(peptide):
                w_ = (prefix_weights[-1] - prefix_weights[i])
                w_ += prefix_weights[j-len(peptide)]
            else:
                w_ = prefix_weights[j] - prefix_weights[i]
            all_weights.append(w_)
    # get full peptide weights
    all_weights.append(prefix_weights[-1])
    return all_weights
    
                

file_path = 'sample_data/theo_sectrum.txt'
# file_path = 'test_data/rosalind_ba4c.txt'
peptide = read_file(file_path)
spec = get_cyclo_spectrum(peptide)
print(' '.join([str(x) for x in sorted(spec)]))