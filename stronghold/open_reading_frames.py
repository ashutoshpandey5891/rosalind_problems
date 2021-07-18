#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 12:49:37 2020

@author: t1
"""

DNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
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


def translate_seq(seq,init_pos = 0):
    return [DNA_Codons[seq[i:(i+3)]] for i in range(init_pos,len(seq)-2,3)]

def reverse_dna(dna_seq):
    # return ''.join([DNA_Reverse[l] for l in dna_seq[::-1]])
    mapping = str.maketrans('ATCG','TAGC')
    return dna_seq.translate(mapping)[::-1]


def gen_reading_frames(seq):
    frames = []
    frames.append(translate_seq(seq,0))
    frames.append(translate_seq(seq,1))
    frames.append(translate_seq(seq,2))
    # reverse sequences
    frames.append(translate_seq(reverse_dna(seq),0))
    frames.append(translate_seq(reverse_dna(seq),1))
    frames.append(translate_seq(reverse_dna(seq),2))
    
    return frames
    
def protiens_from_rf(aa_seq):
    """computes all possible protiens in an amino acid 
       seq and return a list of possible protiens
    """
    
    current_prot = []
    protiens = []
    for aa in aa_seq:
        if aa == '_':
            if current_prot:
                for p in current_prot:
                    protiens.append(p)
                current_prot = []
        else:
            if aa == 'M':
                current_prot.append("")
            for i in range(len(current_prot)):
                current_prot[i] += aa
    return protiens

def all_protiens_from_orfs(seq,startPos = 0,endPos = 0,ordered=False):
    if endPos > startPos:
        refs = gen_reading_frames(seq[startPos:endPos])
    else:
        refs = gen_reading_frames(seq)
        
    all_prots = []
    for ref in refs:
        prots = protiens_from_rf(ref)
        for prot in prots:
            if not prot in all_prots:
                all_prots.append(prot)
    
    if ordered:
        all_prots = sorted(all_prots,key=len,reverse=True)
    
    return all_prots

file_path = 'test_data/rosalind_orf.txt'
dna_dict = read_fasta(file_path)
dna_str = list(dna_dict.values())[0]
all_prots = all_protiens_from_orfs(dna_str)
for prot in all_prots:
    print(prot)
