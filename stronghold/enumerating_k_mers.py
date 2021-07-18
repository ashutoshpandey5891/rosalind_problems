#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:15:08 2020

@author: t1
"""

from itertools import product

def get_k_mers(file_path):
    with open(file_path,'r') as f:
        lines = f.readlines()
    letters = lines[0].strip().split(' ')
    letters.sort()
    n = int(lines[1].strip())
    
    for p in product(letters,repeat = n):
        print(''.join(p))

    

# file_path = 'sample_data/k_mers.txt'
file_path = 'test_data/rosalind_lexf.txt'
get_k_mers(file_path)