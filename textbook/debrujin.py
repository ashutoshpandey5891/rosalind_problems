#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 11:37:12 2020

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

def read_file_m2(file_path):
    pattern_list = []
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            pattern_list.append(line.strip())
    return pattern_list


def get_composition(dna_string,k):
    comp_list = []
    for i in range(len(dna_string)-k+1):
        comp_list.append(dna_string[i:(i+k)])
    return comp_list


def get_debrujin(pattern_lst):
    # pattern_lst = get_composition(dna_string, k)
    key_list = []
    val_list = []
    for pattern in pattern_lst:
        pres = pattern[:-1]
        suff = pattern[1:]
        if pres not in key_list:   
            key_list.append(pres)
            val_list.append([suff])
        else:
            idx = key_list.index(pres)
            val_list[idx].append(suff)
    return key_list,val_list

    
## method 1
# file_path = 'sample_data/debrujin_k.txt'
# # file_path = 'test_data/rosalind_ba3d.txt'
# dna_string,k = read_file(file_path)
# pattern_lst = get_composition(dna_string, k)

## method 2
file_path = 'sample_data/debrujin_km2.txt'
# file_path = 'test_data/rosalind_ba3e.txt'
pattern_lst = read_file_m2(file_path)

## inference
key_list,val_list = get_debrujin(pattern_lst)
sorted_idx = sorted(range(len(key_list)),key = lambda x : key_list[x])
for idx in sorted_idx:
    print('{} -> {}'.format(key_list[idx],','.join(sorted(val_list[idx]))))

