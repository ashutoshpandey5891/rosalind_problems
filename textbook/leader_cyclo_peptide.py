#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:25:27 2021

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


def read_file(file_path):
    N = None
    spectrum = None
    with open(file_path) as f:
        lines = f.readlines()
        N = int(lines[0].strip())
        spectrum = [int(x) for x in lines[1].strip().split(' ')]
    return N,spectrum

MOLE_MASS = {
    'G' : 57,'A':71,'S':87,'P':97,'V':99,'T':101,
    'C' : 103,'I':113,'L':113,'N':114,'D':115,'K':128,
    'Q' : 128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186
    }

mass_list = list(range(57,201))

def expand_cands(cand_list):
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

# @time_it
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
        
    
@time_it
def get_cand_peptide(N,spectrum):
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
        lead_board = expand_cands(lead_board)
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
        
    return lead_cand,lead_score,cand_score_dict
                    


# file_path = 'sample_data/leader_cyclo_peptide.txt'
# file_path = 'test_data/rosalind_ba4g.txt'
# file_path = 'actual_data/dataset_102_10.txt'
# N,spectrum = read_file(file_path)
N = 1000
spectrum = [0, 97, 99, 114, 128, 147, 147, 163, 186, 227, 241, 242, 244, 260, 261, 262, 283, 291, 333, 340, 357, 385, 389, 390, 390, 405, 430, 430, 447, 485, 487, 503, 504, 518, 543, 544, 552, 575, 577, 584, 632, 650, 651, 671, 672, 690, 691, 738, 745, 747, 770, 778, 779, 804, 818, 819, 820, 835, 837, 875, 892, 917, 932, 932, 933, 934, 965, 982, 989, 1030, 1039, 1060, 1061, 1062, 1078, 1080, 1081, 1095, 1136, 1159, 1175, 1175, 1194, 1194, 1208, 1209, 1223, 1225, 1322]

lead_cand,lead_score,score_dict = get_cand_peptide(N, spectrum)
print(lead_cand)

## tyrocidine B1 max score candiidates
max_score = max(score_dict.items(),key=lambda x : x[1])[1]
cands_list = [cand for cand,score in score_dict.items() if score == max_score]
print('Maximum score candidates : ',len(cands_list))
print(' '.join(cands_list))
