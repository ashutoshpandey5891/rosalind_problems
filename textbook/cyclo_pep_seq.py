#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:07:58 2021

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
    spectrum = None
    with open(file_path) as f:
        line = f.read()
        spectrum = [int(s) for s in line.strip().split(' ')]
    return sorted(spectrum)

MOLE_MASS = {
    'G' : 57,'A':71,'S':87,'P':97,'V':99,'T':101,
    'C' : 103,'I':113,'L':113,'N':114,'D':115,'K':128,
    'Q' : 128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186
    }

mass_list = list(set(MOLE_MASS.values()))

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
    
def is_consistent(spectrum,cand):
    '''
    spectrum -> list of ints
    cand -> str of masses eg : '113-129-128-114'
    
    a linear peptide is consistent with Spectrum if every 
    mass in its theoretical spectrum is contained in Spectrum
    '''
    pep_spectrum = get_cand_lin_spectrum(cand)
    for mass in pep_spectrum:
        if pep_spectrum.count(mass) > spectrum.count(mass):
            return False
    return True

@time_it
def get_cyclo_pep_seq(spectrum):
    
    '''
    spectrum -> list of ints
    
    computes all peptides with same spectrum
    as the given spectrum using branch and bound algorithm
    '''
    cand_list = [""]
    final_list = []
    PARENT_MASS = max(spectrum)
    while len(cand_list) > 0:
        cand_list = expand_cands(cand_list)
        # print(cand_list)
        new_cand_list = []
        for i,cand in enumerate(cand_list):
            if get_cand_mass(cand) == PARENT_MASS:
                if get_cand_spectrum(cand) == spectrum:
                    final_list.append(cand)
            elif is_consistent(spectrum, cand):
                new_cand_list.append(cand)
        cand_list = new_cand_list[:]
    return final_list            


# file_path = 'sample_data/cyclo_pep_seq2.txt'
file_path = 'test_data/rosalind_ba4e.txt'
spectrum = read_file(file_path)
final_list = get_cyclo_pep_seq(spectrum)
print(' '.join(sorted(final_list,reverse = False)))