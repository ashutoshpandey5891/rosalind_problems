#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:57:00 2020

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

rna_string = 'AUGCCCGGAGCCUCACAUCUUGAUUCGACCGUUCGCCCGACUACAGCAAGGUUGACCAAAAGCUCUUCUUUUAAAAAUAUUGGUCCUCUAUACUGCAUCAUAGCAGCUGACCACUUCGACAGGUACUGUUACUGCUAUGACAAAAACCCACUUAGCUGGGCUGUGGACCAGGAGCUGUUAAACCGAGGGUUCAGAAUGUCGCGGAGCUGUGGCUUAGACACGCCAGAGGACUACCGGAGGGGGACACUAAUAUCGGCAAGCAGAAAACUAACAUUCAAUGUAGGAUAUGUACACGUGUCCGCAGGAAUUCGAUGUAUGCCCGUGGCACCGUCACAGGUCACGGCCCCGGUCAACGUCGUAACUUUCCCUAGGGGACUGAUUGACGCGGACUAUAUCACGAUCCCCCGAACCCACCGGCAUAAGCGGCACGCGAAAGACACCCUACGUUCUAAGAGGCUCGCCCGGACGUUACGUGAGUUAGUAACCCGUAUUGCGCCCGGCUGUCCCUUUGAUAAGGGGGUGAGUCACAUCGCAAGACCAACAGUUGGAAGCAGGCCGCAGUUGCACGCACGUGCUCGGAGGCUUCCCGGUCUUCAAAUCACUGAGGAACUAGGGGUUUCACCAUACUCCUUACAACACCCCCGGAGAUCACGUUUUCUGAGAAGGUGGAAACGUCUGAUUCUAAGCCGCCCAGAGAACAGAGUCCGUCGAGCAGAUGAUGGUACUCAAGCACCUAUGUGGCGUAUAAUAUCCGAUUCGGGGCCCCUUGCUGAAAGAGGCAUAAUCAUCUUGAGAGCUAAUUGCUAUGUGUCCGUUAUCCGGAAAGCCACGUGGGUUCCGCUAGCAUGCGACAUUUCGAACAGUUCGCCGCAUAGCAAAACGUGGCACAAGGUACAUGACACACAUUAUAGGCUAUAUUCGAACGUUAGGUAUCAUGAUCGCCAGCCACUCCAAUAUGUAAAUUAUGACCAAGGUUCGUGCCGAGCCAUUCAGCGGAGUUUCAAACCGGAGAUAAUCGUAUACUGCAGGAAUGGACCGUGUAGAAGUAAGGUUUUUAAGGAAACUAGAAUAAGAUUCCCGGAGACCGCGAUAUGCAGACUUGAAAGGGGGGUUCUCGCCCAGUUUACGUCCAGGCCCGACCUAAUUAUAGCGCCGGAACGCGCCACUAUCACGAGUACCGCCAGAGCGGAUAGCCCGCCGUUUUUCCUGUUAUGGAAAGUGUACAUGCGGGUCAUUAAGGUCGAGUGCAUUGGAUACAUAAGGAGACUAGUUACGACACGGGAUAGAGAGCUUUCCGUCUUGCGCCACUUGUGGAGUUUCAUUGAGUCUACCGUUCGGCGCUGCAGCGGUAAAGUUGCCUUCGGGAAUAAACACAUCUUGAAGGCGCAACAGCCGAUAUUGAAAGGUGCAAAGAGGGCAGGUGAACCCCUGCAGCGGCGAGAUCAACACAUUACUCCUCUCGCUUAUCGUACCUUUGGCUGUGUGACAGGCGCCAACAGUCACCUAGCCCAGGAGCCCACUUUGUGGACCACUCUAUCGACUUCUAAGCGGCCCUUGGCUAAUUAUCGGCGGCAUAGUGCACUCUGCAUCGACGAUCCAGUGCAAUCGGUAAUGCCGGACGACGCCUCGCCGUUGCAAUUCACACAAUUGAGGGCUUCCUUUUCCCACCAAUUACGUUAUGGCGUGAUCGAGACUCAAUCCUUUUAUUCUAACGUAAUACGCCGUAAGGGUGGUCCACCAGCUUCCACCGUGCCCCACGACAUUAAACUGCGAGCUCCAGGUGGAAUAAACUUAAGGACCCAGCUACAUUUUACAUCCAUAUUUAGGGUCUGGGCUGCUAUGAGUACCGAAGGCAAGCGGCCUGAAUGUCCAAGCCCAUUCUUAGCCUGCCCUAAGCCUGGUGGUGCUAUUCCCUCUCUACUCUACUCGAGGCGUGGUAUAUGGACUGAAAAUCACGCAUUGGAAGCAUUUAUUCAGGAACACGACGGCAUCCCGAUGCAGUUGCCUUUAACGAGCAGGGGGUUUUCAUCCGAUACCGAUUCCCCUGUGUUGGACAUGAACCCGAACUUGUGUAUUACGGCACACACGCGCAAGGGACGUUCCGGUUUACACUAUUGUGAGACGACUUCCAUAUCAGAGGGAUAUAAAUCGCCGCCGAUCGUGUAUUAUGACUUCCAGAAUGUAACCGUGGUUGGGUUACCUGAAGAGCGCUCGUGCAACUAUCUUUGCUCAGUGUGUGGCGUUUGUCUACGCCCUGCGCGUCAGAUGUUACGUUUUCGCCGACCGCCACCCUUGAGGUCUCGCUCCCCAGGACAAGUAUACCUACGGCAGCGCCCGCGCCCCGUGCCGUAUUUCCCGUUUGCAUUGGGCCUCGGGUCCUUUGUUACGUUUCAUUACUCGCGACCACGGUCGGCCGACAUUGACUCGCGUCAGCAACUAUCGCGACCUUAUCUGCUUCGGGCUGUUACUAACGCGAAUCGUCAUAGAUCUGCGUUCCCUCCUUCUAGGCCCAAUCCCACAAAGCACUUUUAUAAAAGCAUGAGACCCAUUUAUGGCGGGGAGAUUCUCAUUACCCAGAUGAGGCGGGGUCUGCACAUGGAUCCGCGAAGUCUAGCUUGGGAAUGGGCGGCUAGAACAUCUGGAUGCAUCCCAAAUUGUAGGGUUUCAGUUUAUUAUGGAGUAGCUAUUGUUUCUCAAGAGGCGGGUAGUAAACUUUACAUUUCACUCGUUGAAGUAGCCGCUUCGGUGAAGAGCCUAGGGUCGGGCUUGUAUAUCCUCAAGCCGAAGCAUUCGCGACAAUCCUCGCCACAACCGUCAUUUGAAAACCUGUUAAGUUUCAACCCCUUGAUUAGGGCUAACGCGCAUGGCAGAUUGACUCUGAAGGACACUGCAGCAUCCUUUAUUUACGCUUACGGCGGAAGUGGCGCUGGGAGCGUCCAAUGGUCCCCGGGCAGGUCCACAGCGUGUACAUCAGCCACAGAUCGACACUCAGGGAACCAACCUGACCGGCACUCUUACAAUCGUCAAAGAUCUAGGGCAGAGGUAGAUAAUAAAUACACUUGGAGACUCUUUACUGCUCUCACCCCGGGCCCUUCUAGUACUGAGACUUUUCGUGAUGGGCGGUUAAUAGGCGGGCUGGGCGCGUUUAACAUACUCAGAAGUACACCCCUCCUGUCCUGCUCGGCCUUGCGAAGACACGCUGUACGCCGAAAUUGGCACAUAUGUGGAGACCGUUUCUCUUCAACGUCCACGUGGGCCACCUUGAGCACCGUCUACCCAACACUUAUAGAAGUUCGUGAGCAGAACGGUUCCAGGUGUACUCCUUCGUUCUCGCGGGCAGUUCUGGCAGCUGCCGAAGCUAAGAACGGUGCCUUGCAGAAUGCCGUUACGACCCUCUACCUCUUUAAGAGGGCACAGAAGCUCCCAGACAUCUCCGUAACUUGGCGGCCCCCAGCCAACGAGUACCAAUGCGUCUCAGGUGCCAAGCCAGGAGAGGCCCUCUUGGUCGACUGCGAGACCCACACUUCCGUGGUGAUUAAGUCCGAUGGAGCAAGAGAGAUCGCCGGCGAUUCAAUAAUUGUAGGUGACUACUCAGCAUCAGCAUAUACAUGCGCUCAUCGACAAACUCUACAACAUUCUGUUCUGUCUUACCCGGUUAGAUGCACGCGAAAUAUACAACUAACUGAUCCCCAAGUAAUCAAGGGGGAGAUGACAUCUGGCCGCAACCUCACAGGGCACACUGCCGAUAUUCCCCACCGGAGAAUAUUCUAUAGGAAGGCCCGGCUACGGACCAUUGCGACUAACACGUUCUGCAUCUUCAUUGUACUUCCAGUUACCAGGUUCCCAUAUUUUAUGAGCGGGACGCAAAAUUUCUUGAGCAACGUACCCUUUACCCACCUGUAUAAUGGAGGACACUGGCUGUAUACUGAAACUUUUCCGUCGGAACGUUCGUACAAUAGCGACGCUUCACACCAGGGUCGUCCCCUAGUGGUAAUACUACCCCCUGAAAGUGUUACACCGAAGCAAGGGUGCGUCGGCACUUCUUUCGCGAUAAUUUUUGGGUCCAGUUUGACCUUGCCAAGAGAAACAGGAUCUGCGAUCACCACUUGUUACACUUUCAUGGUAGUCUCAUUUCUACUAUGUCACAAAUUCAUAUUGAUCAGCCUCAACGAAAGGCACAAGCGGAAUGGAUACAUUUAUCGAGUCAGACUGUGUUCAGUUCCUCAGGAAUGCAUGCACCACCUCCUUAAAGUGAUGUCGACACCGGAACAGGUCUCCGUAGCACCAUCCCUCUUAGUUCAGUGGCAGUUAUCGCUUGCGGUCGCGAAAACAAAAAUCUUAACGGGGAAGCUAGUUAACAAAGAGUCUACCCGUGACCUGAGUGAAAUAAAAAGGCGUAUACGUCAAGGCGGCGAGUGCAUUGAUAUUAAGAUCACGCCGCUGCUCGUCGGGACGAUGAAUAGUGGCAGACUUAUACGUGAUUACACGAGGAUGCGCCAGAUUGUUCGAACCUGGCGGCCAUACAUUGGGGAUCUGCAGGUAUACGUCAAAAUAUGUGCCCGACUGACGCCGCCAACAAGCCCGGAUGAGUGCGGGCCCAUGAUUGACCGUCCCAACCGCAAUCGGUACGUGCUCGAUAAUUCACGGUUACACAGACUAAUCAGGUUCCCCAGGCAGCCAGUCGGGCGAGGUACACAUUGGGGGGAAUUGUAUGUGCACACGCCAAUGCUAGCGUUAUUGCGCGCUAUAUCCCUGACCAAGGGUGGCCUCCUGUCUUUGUCUAGACCCGAGCCCUGGAACGCAAGACGGAAUCGAGUCAAACGCAUAUAUCGACCGAUACGGGCACAUGGAUGGCAUCGCGUUGCGAUGCGUACUCAAUCACAUCCUGGAUACUGGACGGACCUCUCUAUACUAGAACAGACGGCAACACCCCUUUUAUCCGGACGGCACACGUCAUACAAGAAAAUUGCCGGGAUCUACGUACGGCUCGCUUUGCGAGGCACAUCUCGGCUUGCUAUUACGAAUAAGUUCGUAAGGCUUCUAAGUCCCGCUCGUUUUGAGUGCCAAUUUCCCUUCCACAGUCGAUGUAUAAAUCUCCGUCGCACCACGAGCAUGCUCGGGCGUCGUCCUGCGGACCCUUCGCCCAUUCUUGGCGAAGGGUUCAGCACGUCACCGAAACAGUGGCUAAGGCUCUAUAGGCCUGCUGUGUAUGGAAAUCCUUCAGAGUUCAGAUUGGGACUACCCGUUCUACUGAUACCACCGCCUGGAUGUCGUUUAACUACGGAACUGGGCACUUCCAGAAAAGGCUGUUCUACAAGUGCUUCCGAACCCCGAAGUGAAUGCCUACGCCCACUUCCGAGAGCGUUAGUGGUCUUAAGGAUGGAUGACGAUUGUUGGGAGUCGUCUAAUGUUUCACGGACUGUACGGGUAACAGGGCGCUCACCUUUGAGUAAUCGUGGAGUAUCACCUAUGGCGGCUUCGCAACCGUUAUGGAUUACUAGAGCGCUACAGAUGCCUGUGUACUGGCCAUCAUCCUGUUCCGAUCUAAGAGUAAGCCACGUUCCAAAAGUGAGCCCCGGUUGGAGACUCAAGUGUGUCUGGGAUCGUCAUGGCGAAUGCAUUGGACACACAGUCGCUCUUCAAGAUAGUUACGCGGAGGGAGCAAAGGCAUAUCCCCACGUAGGCAAAGACAGCGGCGGCAAGAAGUGGGCACGGGCGCGAUACUCGGAUAGGGGGAUCGACGAAUGGAACUCCCAGCGUACUAGAUUCUAUUGCUUUGGUAGCCCGCAGUUCGAGUCCCUUUACGUUCGAAUUCUCAUCACUCUCUGGUCUCUAUGUUUACCAAUCGCGGCAUGGCAUUUUGACCGCGAUACCACGGAGACUCCAAGGAAAGCGCAGCGGGGCAAGGCCGUUCGUGAACGAAUCUACCCGACUCCUCUUCCGGAUAGCUCAUCGCAUCAGGUGCGAGUACCACAAGGUACUCGAAAUUCGAACAAUGGCUCACCUCCCGAACUUUUGGCAUCGCACCUGGAAAUAGUCAUGGGUUUUAUCGCUAAUCACCAAAGAGGGAGCAUAAUCAUUCGCCUGCUCGACCGCGUAACGAAUAAUCAAGCGGGAGGCUUAGGAGACAUCCUCAUCGUUGUAGCAGGCACAUUUGUCGUAGCUAAAUGGGUACCGUGUAGGUCCACGGAUUGUGUCAAAGGAUGUCCUUCGUCACCUGGCUUUUGCUGUUAUCAACAGAGACGGUUCGGACCAUAUAUAACAAAUAAAUUCGAUACAAACCAGUAUAGCCUCGGGAUACUAGGACUGUACCUCCACCGGCAAAUGCGGUCCUUCAGAAUCGGGAUGCGCCCAAAUUCCGAUGUUUGUGCCGCCCGCUCCGCCAAGCGAGUGGGAAGCACUGAGGCUCAGAAAGUGGGGAACGGAUACCCUGAAUGUCAAAGAGGUGAGAAACCAUACUUUACUGGCCUGUACGUCCCCAAGGAUGAGCAAAGUGCUGUCUCCAUGCAUGCGGUAGUCCCAUAUAUCGACCAUACUUGGGCUGCCGAAGCGUCCCUAUUUUCGCACUUUGUAGCUUCUUCCAAACCGCGACUUGGGUUUCGCGUGGUGUCGGAUUUACUCAGGAUUCCCACACGGUUGCUUAAGGACUGGCAGAAGCCUGGCUCAUCACAUGCUACACCUUUCGCGCCCUUCCUGAAAGCGCAUGAUGGUCCAAGAUCAGUUUCUAUAAUGUCCUGCCUGAUAGUCCUCGCCCGAGGCUUUGUUCAACGACUACGAGCCAGAUCCUCGUGGGCGCAGAAGCACACAAAAGAUUCACUCACCUGUGGAACAGGACUCAACUAUCGAGGCAUCUUCGGUGUCACAGGCAUAAUAAGGUCACGUUCCAGGAUGGGACGGAUUAAUCAGAUGGUGAUUCAGCCUGUACUCAGGACGGCCACCCUUCACUCGCACGAGGGUGGAGUUACCGGCCUCUUAAUAAUACUCGAGCAGUCUAGCUGCGAGACGGGAAUCUGGGUAAUAGUCAAUGCGGUAGAGAAUAUUCCCGACUGCAGACACAGGAGUCCAGGUGGCCGUGACCACAGGUUGUGCAAACUUACGGGUGCGCUGAAACUAGUUGGUUCCUUAUGCAUAAAAGUCUUGCGUAAUUCUCUCAUAUGUGCUAUACAAUGGAGUGCUACCCGCACCAAUAAACCCAAUAAGGAACCAUUGUCGUACAUAGCGUCUCGUUCAAGGCCUGCCGACUCGAGAGCUAACAGACGGUGGAGAAUGGGUGUGUCUCUCAACUCGGCGUUGAAAGGUCUGCUGCAUCGCCUUCGUAAGGUUGGGCGCGAUUGUUUAGGCGGAAUUCGGGGGUUCUGCACGGGGGCAACGAGAAUGUCCGCCCAAUCUUCCACGGGCCUUCCCCAUAAAUCAGUACUAGUCGGAGUCCUGCACAAUCAGAUUCGAAUUUCCACCACGAUACUGAACGAGACAAGCUGUAGGAACAGCGGCAUUUGGCUAUUCCAACACUACGCCGUGCAGCGGGCCAUUAACACAGCAACAUAUGACGCUAUUUCUAGCCACAUUCAGCCAUGCAAAGUACCCCGAGAAGUCAACUCACCGGCAGUCACCCUCCCGGCAGGACACACCUCGCCCGACUGUGGGUCGCUAAGUCUCAAUAGUACCCGGCACGGGAACCAGUAUUGUGAAACCAUCCAGGAGGACCUUAGUCAUAGAUGGCAAGUCAUCUGUCUUUUUUUGAGAUCAAGUAUCAAUGCUAUUCCGGAGGGUGAAGAACUGAAAGAUGUUAUGCCGUCGAGGCAGGAAUCGACUUGGUACAUAGUAGCAUCGACGACCCAGCGCAAAGUACCAUAUCCUCUGAAACCGUUGUCAGGAACACUAUGCUCGAGGGGGAAGUGCACAAACGAGUCCCUAGCUACUAGAAACGGUACGAUGCUCCGGUCGCUCGUCCGCGGGGAUCUCCCCAAUCCUAACGGGGGUGUUACGACGUUAUCUCUUAAGCUUGCGAGUAUACGCAUACUUGAGUCGAAUAAUGUCCAUCCGCACCCAAGGCAAUGGGCUGACUCUCCAAGGGACAUAUACAGCCAUGCCGCAAUCAAGCUGCCUGUGCUCGUGAUUCAUGCAGCCAGUUGUAUGGCUAUCAUUCUUGGACGUACAAGAAGUCCAUGCAUCUUCUCCACUCCGGACUCUCUGCUUCUCCAACAUUGUUGCUACGUCUCGAUUGCGACACGCAGUUAUUCUCUCGAUAAACAGAGUCGGACAUCCGUCAGACGCAUUGAAGCACGUUGUCAGAACCGCAUGUCCAUUCAAGUAUGGGCUUUCCGAAACGUCGGGAGGCUGUUUAGUCUCCCGUUAUUUAACCGGAGCGUAAACGGGAACUUGUUGUCACUUACCGCUAGUGUAUGA'
prots = []
all_prots = []

# for i in range(0,len(rna_string),3):
#     rna_codon = rna_string[i:(i+3)]
#     # print(rna_codon)
#     p_ = RNA_Codons.get(rna_codon)
#     if p_ == "_":
#         for prot in prots:
#             all_prots.append(prot)
#         prots = []
#     else:
#         if p_ == 'M':
#             prots.append("")
#         for i in range(len(prots)):
#             prots[i] += p_

prot = ''
for i in range(0,len(rna_string),3):
    rna_codon = rna_string[i:(i+3)]
    p_ = RNA_Codons.get(rna_codon)
    prot += p_
    
    
print(prot)
        