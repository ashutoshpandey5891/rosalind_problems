#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:48:25 2020

@author: t1
"""

def readFile(file_path):
    with open(file_path,'r') as f:
        return [l.strip() for l in f.readlines()]
    
    
def gc_content(dna_seq):
    return ((dna_seq.count('C') + dna_seq.count('G')) / len(dna_seq)*100)

file_path = 'test_data/gc_content_test.txt'
dna_list = readFile(file_path)
dna_dist = {}
label = ''

for line in dna_list:
    if '>' in line:
        label = line.replace('>','')
        dna_dist[label] = ''
    else:
        dna_dist[label] += line
 
res_dict = {key:gc_content(value) for key,value in dna_dist.items()}
max_key = max(res_dict,key = res_dict.get)
max_gc = res_dict[max_key]
        
print(f'{max_key}\n{max_gc:.6f}')
        