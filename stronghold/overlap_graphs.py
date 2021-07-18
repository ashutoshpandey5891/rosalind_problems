#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:59:02 2020

@author: t1
"""

def read_fasta(file_path):
    dna_seqs = {}
    with open(file_path,'r') as f:
        lines = f.readlines()
        cur_seq = ''
        cur_seq_name = ''
        for line in lines:
            if not line.startswith('>'):
                cur_seq += line.strip()
            else:
                if cur_seq != '' and cur_seq_name != '':
                    dna_seqs[cur_seq_name] = cur_seq
                cur_seq_name = line.replace('>','').strip()
                cur_seq = ''
        if cur_seq != '':
            dna_seqs[cur_seq_name] = cur_seq
    return dna_seqs

def readFile(file_path):
    with open(file_path,'r') as f:
        return [l.strip() for l in f.readlines()]

def read_fasta1(file_path):
    dna_list = readFile(file_path)
    dna_dist = {}
    label = ''
    
    for line in dna_list:
        if '>' in line:
            label = line.replace('>','')
            dna_dist[label] = ''
        else:
            dna_dist[label] += line
    return dna_dist


def get_adjacent_list(seq_dict,k):
    all_adjac = []
    seq_names = list(seq_dict.keys())
    for i in range(len(seq_names)-1):
        name_i = seq_names[i]
        seq_i = seq_dict[name_i]
        
        for j in range((i+1),len(seq_names)):
            name_j = seq_names[j]
            seq_j = seq_dict[name_j]
            if seq_i != seq_j:
                if (seq_i[-k:] == seq_j[:k]):
                    all_adjac.append([name_i,name_j])
                if (seq_j[-k:] == seq_i[:k]):
                    all_adjac.append([name_j,name_i])
    return all_adjac

# def get_adjacent_list(seq_dict,k=3):
#     all_adjac = []
#     seq_names = list(seq_dict)
#     for i in range(len(seq_names)):
#         name_i = seq_names[i]
#         seq_i = seq_dict[name_i]
#         for j in range(len(seq_names)):
#             name_j = seq_names[j]
#             seq_j = seq_dict[name_j]
#             if (seq_i != seq_j):
#                 if (seq_i[-k:] == seq_j[:k]) or (seq_j[-k:] == seq_i[:k]):
#                     if ((name_i,name_j) not in all_adjac) and ((name_j,name_i) not in all_adjac):
#                         all_adjac.append((name_i,name_j))
#     return all_adjac

file_path = 'test_data/rosalind_grph.txt'
seq_dict = read_fasta(file_path)
adjacs = get_adjacent_list(seq_dict,3)
print(len(adjacs))
for ad in adjacs:
    print(f'{ad[0]} {ad[1]}')