#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 00:37:12 2020

@author: t1
"""


def pattern2number(pattern):
    k = len(pattern)
    dna_list = ['A','C','G','T']
    number = 0
    for i in range(k):
        p = pattern[i]
        idx = dna_list.index(p)
        
        number += idx*4**(k-1-i)
    return number
# print(pattern2number('ATGCAA'))  
        
def number2pattern(number,k):
    dna_list = ['A','C','G','T']
    pat = ''
    for i in range(k-1,-1,-1):
        idx = int(number/4**(i))
        number = number % (4**i)
        pat += dna_list[idx]
        
    return pat

def computeFreqs(dna_seq,k):
    freq_arr = [0]*(4**k)
    for i in range(len(dna_seq)-k+1):
        pat = dna_seq[i:(i+k)]
        num = pattern2number(pat)
        freq_arr[num] += 1
    return freq_arr
# print(number2pattern(5437, 8))


def read_file1(file_path):
    '''Read file funciton for  Compute frequencies'''
    dna_seq = ''
    k = 0
    with open(file_path) as f:
        lines = f.readlines()
        dna_seq = lines[0].strip()
        k = int(lines[1].strip())
    return dna_seq,k

def read_file2(file_path):
    '''read file for patter2number '''
    
    dna_seq = ''
    with open(file_path) as f:
        dna_seq = f.read().strip()
    return dna_seq

def read_file3(file_path):
    '''read file for number2pattern'''
    num = None
    k = None
    with open(file_path) as f:
        lines = f.readlines()
        num = int(lines[0].strip())
        k = int(lines[1].strip())
    return num,k
    
# file_path = 'sample_data/number2pattern.txt'
file_path = 'test_data/rosalind_ba1m.txt'
# file_path = 'sample_data/temp_data.txt'
num,k = read_file3(file_path)
print(number2pattern(num, k))