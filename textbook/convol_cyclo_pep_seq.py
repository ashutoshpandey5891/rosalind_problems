#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:49:28 2021

@author: t1
"""

import time
import numpy as np
from collections import Counter

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.clock()
        result = func(*args,**kwargs)
        end = time.clock()
        print(' {} executed in time : {:.6f} sec'.format(func.__name__,end - start))
        return result
    return wrapper

def read_file(file_path):
    M = None
    N = None
    spectrum = None
    with open(file_path) as f:
        lines = f.readlines()
        M = int(lines[0].strip())
        N = int(lines[1].strip())
        spectrum = [int(x) for x in lines[2].strip().split(' ')]
    return M,N,sorted(spectrum)

def get_convolution2(spectrum):
    '''
    spectrum -> list of ints
    
    returns :
        conv_list -> list of ints; convolution of spectrum
    '''
    spec_arr = np.array(spectrum)
    conv_mat = spec_arr.reshape(-1,1) - spec_arr.reshape(1,-1)
    conv_list = list(conv_mat[conv_mat > 0].ravel())
    return conv_list

def get_top_M_weights(M,conv_list):
    '''
    M -> int
    conv_list -> list of ints ; 
    
    returns -> top M most common values in convolution 
    '''
    conv_list = [el for el in conv_list if (el >= 57) and (el <= 200)]
    counts_ = Counter(conv_list)
    mc_list = counts_.most_common(M)
    last_count_val = mc_list[-1][1]
    for (key,val) in counts_.items():
        if (val == last_count_val) and ((key,val) not in mc_list):
            mc_list.append((key,val))
    return [w for (w,c) in mc_list]
          
def expand_cands(cand_list,mass_list):
    '''
    cand_list -> list of strs
    
    returns new collection containing all possible extensions of 
    peptides in Peptides by a single amino acid mass
    '''
    new_cand_list = []
    for cand in cand_list:
        for mass in mass_list:
            if cand == "":
                new_cand = str(mass)
            else:    
                new_cand = cand + '-' + str(mass)
            new_cand_list.append(new_cand)
    return new_cand_list

def get_cand_mass(cand):
    '''
    cand -> str
    returns total mass for candidate sequence
    '''
    mass_list = [int(m) for m in cand.split('-')]
    return sum(mass_list)

def get_cand_spectrum(cand):
    
    '''
    cand -> str of masses eg : '113-129-128-114'
    returns cyclo spectrum of peptides
    '''
    mass_list = [int(m) for m in cand.split('-')]
    spectrum = []
    for mass in mass_list:
        spectrum.append(mass)
    for k in range(2,len(mass_list)):
        for i in range(len(mass_list)):
            j = i+k
            w_ = None
            if j > len(mass_list):
                w_ = sum(mass_list[i:]) + sum(mass_list[:(j - len(mass_list))])
            else:
                w_ = sum(mass_list[i:j])
            spectrum.append(w_)
    if len(mass_list) > 1:
        spectrum.append(sum(mass_list))
    spectrum = [0] + spectrum
    return sorted(spectrum)
            
def get_cand_lin_spectrum(cand):
    mass_list = [int(m) for m in cand.split('-')]
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

def get_cand_cyclic_score(peptide,spectrum):
    '''
    peptide -> str
    spectrum -> list of ints
    score is defined as the number of masses shared between 
    Cyclospectrum(Peptide) and Spectrum
    '''
    peptide_spectrum = get_cand_spectrum(peptide)
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

def get_cand_peptide(N,spectrum,mass_list):
    '''
    N -> leaderboard size
    spectrum -> experimental spectrum
    returns peptide cancdidate with the highest score
    '''
    
    lead_board = [""]
    lead_board_trim = []
    lead_cand = ''
    lead_score = 0
    cand_score_dict = {}
    PARENT_MASS = max(spectrum)
    while len(lead_board) > 0:
        lead_board = expand_cands(lead_board,mass_list)
        lead_board_trim = []
        
        for cand in lead_board:
            cand_mass = get_cand_mass(cand)
            # cand_score = get_cand_cyclic_score(cand, spectrum)
            # cand_score_dict[cand] = cand_score
            if cand_mass == PARENT_MASS:
                cand_score = get_cand_cyclic_score(cand, spectrum)
                cand_score_dict[cand] = cand_score
                
                if cand_score > lead_score:
                    lead_cand = cand
                    lead_score = cand_score
            if cand_mass <= PARENT_MASS:
                lead_board_trim.append(cand)
        lead_board = trim(N,lead_board_trim,spectrum)
        
    return lead_cand

@time_it
def get_conv_cyclo_pep_seq(M,N,spectrum):
    '''
    M -> int ; top M most frequent weight values are taken from convolution of spectrum
    N -> int ; trim top N values in leaderboard cyclopeptide sequencing 
    spectrum -> list of ints ; experimental spectrum
    
    returns : most probable sequence of peptide
    '''
    # get spectrum convolution
    conv_list = get_convolution2(spectrum)
    mass_list = get_top_M_weights(M, conv_list)
    # print('masses : ',len(mass_list),mass_list)
    
    lead_cand = get_cand_peptide(N, spectrum, mass_list)
    return lead_cand


# file_path = 'sample_data/convol_cyclo_pep_seq.txt'
file_path = 'test_data/dataset_104_7.txt'
M,N,spectrum = read_file(file_path)
lead_cand = get_conv_cyclo_pep_seq(M, N, spectrum)
print(lead_cand)