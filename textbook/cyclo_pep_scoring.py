#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 10:03:40 2021

@author: t1
"""

import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.clock()
        result = func(*args,**kwargs)
        end = time.clock()
        print(' {} executed in time : {:.6f} sec'.format(func.__name__,end - start))
        return result
    return wrapper

MOLE_MASS = {
    'G' : 57,'A':71,'S':87,'P':97,'V':99,'T':101,
    'C' : 103,'I':113,'L':113,'N':114,'D':115,'K':128,
    'Q' : 128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186
}

def read_file(file_path):
    peptide = None
    spectrum = []
    with open(file_path) as f:
        lines = f.readlines()
        peptide = lines[0].strip()
        spectrum = [int(x) for x in lines[1].strip().split(' ')]
    return spectrum,peptide

def get_cyclo_spectrum(peptide):
    '''
    peptide -> str
    returns cyclic spectrum of peptide
    '''
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


def get_score(peptide,spectrum):
    '''
    peptide -> str
    spectrum -> list of ints
    score is defined as the number of masses shared between 
    Cyclospectrum(Peptide) and Spectrum
    '''
    peptide_spectrum = get_cyclo_spectrum(peptide)
    pep_spectrum_set = list(set(peptide_spectrum))
    score = 0
    for mass in pep_spectrum_set:
        count_1 = peptide_spectrum.count(mass)
        count_2 = spectrum.count(mass)
        score += min(count_1,count_2)
    return score

# file_path = 'sample_data/cyclo_pep_scoring.txt'
file_path = 'test_data/rosalind_ba4f.txt'
spectrum,peptide = read_file(file_path)
score = get_score(peptide,spectrum)
print(score)
    
    
    