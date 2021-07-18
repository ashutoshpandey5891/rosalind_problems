#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:26:29 2020

@author: t1
"""

import itertools

def read_file(file_path):
    with open(file_path,'r') as f:
        n = int(f.read().strip())
    return n

def get_gene_orderings(n):
    tmp = [(-i,i) for i in range(1,n+1)]
    perms_ls = list(itertools.product(*tmp))
    all_perms = []
    for p in perms_ls:
        px = list(itertools.permutations(p,n))
        for x in px:
            if x not in all_perms:
                all_perms.append(x)
    return all_perms
    
        


# file_path = 'sample_data/eogo.txt'
file_path = 'test_data/rosalind_sign.txt'
n = read_file(file_path)
res = get_gene_orderings(n)
print(len(res))
for r in res:
    print(' '.join([str(x) for x in list(r)]))