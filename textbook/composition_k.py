#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:19:56 2020

@author: t1
"""

def read_file(file_path):
    dna_string = None
    k = None
    with open(file_path) as f:
        lines = f.readlines()
        k = int(lines[0].strip())
        dna_string = lines[1].strip()
    return dna_string,k

def get_composition(dna_string,k):
    comp_list = []
    for i in range(len(dna_string)-k+1):
        comp_list.append(dna_string[i:(i+k)])
    return comp_list


# file_path = 'sample_data/composition_k.txt' #sample
# file_path = 'test_data/dataset_197_3.txt'   #stepik
file_path = 'test_data/rosalind_ba3a.txt'
dna_string,k = read_file(file_path)
comp_list = get_composition(dna_string, k)
print('\n'.join(comp_list))