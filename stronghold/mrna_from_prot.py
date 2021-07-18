#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 12:43:34 2020

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

prot2rna = {}

for codon,prot in RNA_Codons.items():
    if not prot in prot2rna:
        prot2rna[prot] = []
    prot2rna[prot].append(codon)
    
# print(sum([len(cod_list) for cod_list in prot2rna.values()]))



def get_nrnas(prot_str,last = False):
    total_rnas = 1
    for prot in prot_str:
        total_rnas *= len(prot2rna[prot])
    if last:
        total_rnas *= len(prot2rna['_'])
    return total_rnas


def get_nrnas_long_prot(prot_seq,k=10,n=1000000):
    total_rnas = 1
    # k -> number of letters taken at a time
    # n -> 
    rng = len(prot_seq)
    full_seq = ''
    for i in range(0,rng,k):
        temp_seq = prot_seq[i:min(i+k,len(prot_seq))]
        full_seq += temp_seq
        nrnas = get_nrnas(temp_seq,last = False) % n
        
        total_rnas *= nrnas
    total_rnas *= 3
    return total_rnas % n,full_seq
    

prot_str = 'MKNTTIAYRIKDTTDKKFTDSAHWMSWSMFDPTCKKDHENHKRWTACSKRAMHGMHSRFGHAGIVNIHRPMGRLTTHRHLWYLHWDHLNLWIRPNLAGAPNRHSWNPWHDMYDPEVGFLVFWSFGVITGFFMSDMAKFEFSNRGVYNNHYTCAWMSSDLMMQSFCCHLNLRMWCYMSSDLQSAQVVKPVNTCCTIDCNPYYDWLLVDALLGHKKGIFCANWEPTRVHRALMDRVDIAMWKKPEEAYIEILKTALPKQFFIKHPFLNALAMCGTNKKWHMHKFKKICQSSAERMTNGNCSYWHKRIIYWPIQSMPINAAWCCPVQYIFAKIAVSGVGIDNDYVIIMDVISAEQPCVNVNPGGMIYSNFKGAWFLNKRNCNFQLVGRPRWPIGYLHNSDHIKWPPMYKKAEAHFDHYCTRRYAKAPPRPKWHHVIIGNNCSQMPNCNDTRKARRGAYFKDRIHCDTYPDLDKEGRKLYMANDMKESRAQCMKRMPTCKGNEPKLWTMDVFTQYYYRNSCRCPIDINVYSMEEKQECSQAQAQKMNWGMLGFPVVVTSKKCFQGTTRGYALSASQPHSIVHPEFHEWHLNDGRSRHATPEISCCNHWIEMGRPDQAFRYREMRHMHWQVQGERSHISTWIGLQRTRHRTMLDGTNCCVAWNLSQCRNRILKDPTCKGGCWDNMWQFIRGHFGGRVANMTTVLYVYMAIRCGDKGCAWTYVRDWVHCIIKDGYWHHAYYWSMVPCPLPMVPHYKVEGREVSGQRQIECGTSHLMFNISCPSTYYMVDMVQYDNYWIKQMFQHWQSMFQHFFRQNMREIDLERNMYMYELCMDTGKKMVSFVPRAECVWIESGKIQGWMQIWGAEVSFTWNCLMIASYTQGQECRICRWDDNELYINFKFWTGGWNYPQYDGIVKSIIHPMCMCFPRGNLILMWATCGTHDGMWLEGEAKILEYGKVMHWEGCMDVCMTYPWPNPKKENWIDTPQPVQQNIMMQENQHNESTIFS'
t,full_seq = get_nrnas_long_prot(prot_str)
print(t)