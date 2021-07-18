#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:52:27 2021

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

def read_file(file_path):
    rna_string = ''
    with open(file_path) as f:
        rna_string = f.read().strip()
    return rna_string

def translate(rna_str):
    prot_list = []
    for i in range(0,len(rna_str),3):
        codon = rna_str[i:(i+3)]
        prot = RNA_Codons[codon]
        # print(codon,prot)
        if prot == '_':
            # print('stop codon')
            break
        elif prot == 'M':
            prot_list.append('')
            for i in range(len(prot_list)):
                prot_list[i] += prot
        else:
            for i in range(len(prot_list)):
                prot_list[i] += prot
    return prot_list
        
def get_longest(rna_string):
    prots = translate(rna_string)
    return sorted(prots,key=lambda x : len(x),reverse = True)[0]

# file_path = 'sample_data/translation.txt'
file_path = 'test_data/rosalind_ba4a.txt'
rna_string = read_file(file_path)
prot_str = get_longest(rna_string)
print(prot_str)
