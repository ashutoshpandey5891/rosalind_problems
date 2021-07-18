#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:17:09 2021

@author: t1
"""

import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.clock()
        result = func(*args,**kwargs)
        end = time.clock()
        print(' {} executed in time : {:.6f} sec'.format(func.__name__,end - start))
        return result
    return wrapper

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
    dna_string = ''
    peptide = ''
    with open(file_path) as f:
        lines = f.readlines()
        dna_string = lines[0].strip()
        peptide = lines[1].strip()
    return dna_string,peptide

def transcription(dna_seq):
    # converts dna string to rna string
    return dna_seq.replace('T','U')


def reverse_dna(dna_seq):
    # get the reverse compliment of a dna_string
    mapping = str.maketrans('ATCG','TAGC')
    return dna_seq.translate(mapping)[::-1]

def get_reading_frames(dna_string):
    frames = []
    frames.append(dna_string[0:])
    frames.append(dna_string[1:])
    frames.append(dna_string[2:])
    frames.append(reverse_dna(dna_string[0:]))
    frames.append(reverse_dna(dna_string[1:]))
    frames.append(reverse_dna(dna_string[2:]))
    return frames

def translate(dna_str):
    rna_str = transcription(dna_str)
    return ''.join(RNA_Codons[rna_str[i:(i+3)]] for i in range(0,len(rna_str),3))


@time_it
def get_peptide_encoding(dna_str,peptide):
    pep_len = len(peptide)
    dna_sub_len = pep_len*3
    encodes = []
    for start_idx in range(3):
        for i in range(start_idx,len(dna_str) - dna_sub_len,3):
            substr = dna_str[i : (i+dna_sub_len)]
            if len(substr) % 3 == 0:
                if translate(substr) == peptide or translate(reverse_dna(substr)) == peptide:
                    encodes.append(substr)
    return encodes
                
    


# file_path = 'sample_data/peptide_encoding.txt'
# file_path= 'test_data/rosalind_ba4b.txt'
# dna_string,peptide = read_file(file_path)

dna_string = open('actual_data/Bacillus_brevis.txt').read().strip().replace('\n','')
peptide = 'VKLFPWFNQY'
encodes = get_peptide_encoding(dna_string, peptide)
# print('\n'.join(encodes))
print(len(encodes))