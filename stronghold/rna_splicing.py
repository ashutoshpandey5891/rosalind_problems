#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:24:19 2020

@author: t1
"""

RNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUA": "I", "AUU": "I", "AUC": "I",
    "AAA": "K", "AAG": "K",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "_", "UAG": "_", "UGA": "_"
}

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



def remove_introns(dna_dict):
    dna_seqs = list(dna_dict.values())
    dna_seqs.sort(key = lambda x : len(x),reverse = True)
    
    dna_seq = dna_seqs[0]
    introns = dna_seqs[1:]
    for intron in introns:
        dna_seq = dna_seq.replace(intron,'')
    return dna_seq

def dna2prot(dna_seq):
    rna_seq = dna_seq.replace('T','U')
    # print(rna_seq)
    all_prots = []
    cur_prots = []
    for i in range(0,len(rna_seq),3):
        codon = rna_seq[i:(i+3)]
        prot_ = RNA_Codons[codon]
        if prot_ == '_':
            for p in cur_prots:
                if p not in all_prots:
                    all_prots.append(p)
            cur_prots = []
        else:
            if prot_ == 'M':
                cur_prots.append('')
            for i in range(len(cur_prots)):
                cur_prots[i] += prot_
    return all_prots
    


# file_path = 'sample_data/rna_splicing.txt'
file_path = 'test_data/rosalind_splc.txt'
dna_dict = read_fasta(file_path)
dna_seq = remove_introns(dna_dict)
all_prots = dna2prot(dna_seq)
all_prots.sort(key = lambda x : len(x),reverse = True)
print(all_prots[0])
