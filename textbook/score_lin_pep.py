#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:20:56 2021

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

def read_file1(file_path):
    peptide = None
    with open(file_path) as f:
        lines = f.readlines()
        peptide = lines[0].strip()
    return peptide

def read_file2(file_path):
    peptide = None
    spectrum = None
    with open(file_path) as f:
        lines = f.readlines()
        peptide = lines[0].strip()
        spectrum = [int(x) for x in lines[1].strip().split(' ')]
    return spectrum,peptide

def read_file3(file_path):
    lead_board = None
    spectrum = None
    N = None
    with open(file_path) as f:
        lines = f.readlines()
        lead_board = [x.strip() for x in lines[0].strip().split(' ')]
        spectrum = [int(x) for x in lines[1].strip().split(' ')]
        N = int(lines[2].strip())
    return N,lead_board,spectrum

MOLE_MASS = {
    'G' : 57,'A':71,'S':87,'P':97,'V':99,'T':101,
    'C' : 103,'I':113,'L':113,'N':114,'D':115,'K':128,
    'Q' : 128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186
    }

def get_cand_lin_spectrum(cand):
    mass_list = [MOLE_MASS[x] for x in cand]
    spectrum = []
    for mass in mass_list:
        spectrum.append(mass)
    for k in range(2,len(mass_list)):
        for i in range(len(mass_list) -k +1):
            j = i+k
            w_ = sum(mass_list[i:j])
            spectrum.append(w_)
    if len(mass_list) > 1:
        spectrum.append(sum(mass_list))
    spectrum = [0] + spectrum
    return sorted(spectrum)

def get_cand_lin_score(peptide,spectrum):
    '''
    peptide -> str
    spectrum -> list of ints
    score is defined as the number of masses shared between 
    Cyclospectrum(Peptide) and Spectrum
    '''
    peptide_spectrum = get_cand_lin_spectrum(peptide)
    pep_spectrum_set = list(set(peptide_spectrum))
    score = 0
    for mass in pep_spectrum_set:
        count_1 = peptide_spectrum.count(mass)
        count_2 = spectrum.count(mass)
        score += min(count_1,count_2)
    return score

def trim(N,lead_board,spectrum):
    if len(lead_board) == 0:
        return []
    score_list = [(cand,get_cand_lin_score(cand, spectrum)) for cand in lead_board]
    sorted_score_list = sorted(score_list,key = lambda x : x[1],reverse = True)
    # print(sorted_score_list)
    trimmed_list = sorted_score_list[:N]
    nt_score = trimmed_list[-1][1]
    for cand,score in sorted_score_list[N:]:
        if score == nt_score:
            trimmed_list.append((cand,score))
    trimmed_cand_list = [x[0] for x in trimmed_list]
    # print(len(trimmed_cand_list))
    return trimmed_cand_list

### problem 1
# file_path = 'test_data/rosalind_ba4j.txt'
# peptide = read_file1(file_path)
# spectrum = get_cand_lin_spectrum(peptide)
# print(' '.join([str(x) for x in spectrum]))

### problem 2
# file_path = 'sample_data/score_lin_pep.txt'
# file_path = 'test_data/rosalind_ba4k.txt'
# spectrum,peptide = read_file2(file_path)
# score = get_cand_lin_score(peptide, spectrum)
# print(score)

### problem 3
# file_path = 'sample_data/trim_linear.txt'
file_path = 'test_data/rosalind_ba4l.txt'
N,lead_board,spectrum = read_file3(file_path)
trimmed_list = trim(N,lead_board,spectrum)
print(' '.join(trimmed_list))