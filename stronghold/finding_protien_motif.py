#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:15:41 2020

@author: t1
"""

import re
import requests

def read_uniprot_fasta_file(file_path):
    prot_seq = ''
    prot_name = ''
    with open(file_path,'r') as f:
        for line in f.readlines():
            if line.startswith('>'):
                prot_seq = ''
                prot_name = line.split('|')[1].strip()
            else:
                prot_seq += line.strip()
                
    return prot_seq,prot_name

def read_uniprot_fasta_url(prot_name):
    fasta_url = f'https://www.uniprot.org/uniprot/{prot_name}.fasta'
    resp = requests.get(fasta_url)
    seq_str = resp.content.decode().strip().split('\n')
    prot_seq = ''
    prot_name = ''
    for line in seq_str:
        if line.startswith('>'):
            prot_seq = ''
            prot_name = line.split('|')[1].strip()
        else:
            prot_seq += line.strip()
    return prot_seq

def get_prot_seqs(file_path):
    prot_names = None
    with open(file_path,'r') as f:
        prot_names = [line.strip() for line in f.readlines()]
    prot_dict = {}
    for prot_name in prot_names:
        prot_dict[prot_name] = read_uniprot_fasta_url(prot_name)
    return prot_dict


def match_n_glycosylation_motif(prot_seq):
    '''
    tests if a protien seq has the n_glycosylation_protien given as N{P}[ST]{P}
    '''
    motif_str = r'N[^P][ST][^P]'
    # start_points = [m.start() + 1 for m in re.finditer(motif_str,prot_seq)]
    start_points = []
    for i in range(len(prot_seq)-len(motif_str)):
        prot_subseq = prot_seq[i : (i + len(motif_str))]
        if re.match(motif_str,prot_subseq):
            start_points.append(i+1)
    return start_points

def main(file_path):
    prot_dict = get_prot_seqs(file_path)

    for key,val in prot_dict.items():
        res_list = match_n_glycosylation_motif(val)
        res_str = ' '.join([str(m) for m in res_list])
        if not res_str == '':
            print(key)
            print(res_str)

if __name__ == '__main__':
    file_path = 'sample_data/rosalind_mprt.txt'
    main(file_path)

