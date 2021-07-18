#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 14:27:58 2021

@author: t1
"""

def read_file(file_path):
    k = None
    d = None
    read_pairs = []
    with open(file_path) as f:
        lines = f.readlines()
        k,d = lines[0].strip().split(' ')
        k = int(k.strip())
        d = int(d.strip())
        for line in lines[1:]:
            read_pairs.append(line.strip())
    return read_pairs,k,d

def get_string_form_pairs_path(read_pairs,k,d):
    pref,suff = read_pairs[0].split('|')
    pref_string = pref
    suff_string = suff
    for pair in read_pairs[1:]:
        pref,suff = pair.split('|')
        pref_string += pref[-1]
        suff_string += suff[-1]
    dna_string = pref_string + suff_string[-(k+d):]
    return dna_string


# file_path = 'sample_data/string_spelled_gapped.txt'
file_path = 'test_data/rosalind_ba3l.txt'
read_pairs,k,d = read_file(file_path)
dna_str = get_string_form_pairs_path(read_pairs, k, d)
print(dna_str)