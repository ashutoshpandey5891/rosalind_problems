#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 12:40:18 2020

@author: t1
"""
import numpy as np



def read_fasta(file_path):
    dna_seqs = []
    with open(file_path,'r') as f:
        lines = f.readlines()
        cur_seq = ''
        for line in lines:
            if not line.startswith('>'):
                cur_seq += line.strip()
            else:
                if cur_seq != '':
                    dna_seqs.append(cur_seq)
                cur_seq = ''
        if cur_seq != '':
            dna_seqs.append(cur_seq)
    return dna_seqs


def get_concensus(dna_seqs):
    N = len(dna_seqs[0])
    for seq in dna_seqs:
        if len(seq) != N:
            print('Invalid seq length')
            return None
    As,Cs,Gs,Ts = np.zeros(N),np.zeros(N),np.zeros(N),np.zeros(N)
    for i in range(N):
        for seq in dna_seqs:
            if seq[i] == 'A':
                As[i] += 1
            elif seq[i] == 'C' :
                Cs[i] += 1
            elif seq[i] == 'G':
                Gs[i] += 1
            elif seq[i] == 'T':
                Ts[i] += 1
    
    all_mat = np.concatenate((As.reshape(-1,1),Cs.reshape(-1,1),Gs.reshape(-1,1),Ts.reshape(-1,1)),axis=1)
    cons_arr = np.argmax(all_mat,axis=1)
    cons_srt = ''
    for idx in cons_arr:
        cons_srt += ['A','C','G','T'][idx]
    print(cons_srt)
    all_mat = all_mat.T
    ans_str = ''
    for i in range(all_mat.shape[0]):
        ans_str += ['A:','C:','G:','T:'][i]
        for j in range(all_mat.shape[1]):
            ans_str += ' {}'.format(int(all_mat[i,j]))
        ans_str += '\n'
    print(ans_str)
        
file_path = 'test_data/rosalind_cons.txt' 
dna_seqs = read_fasta(file_path)
get_concensus(dna_seqs)