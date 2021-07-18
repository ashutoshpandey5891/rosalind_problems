#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 00:37:12 2020

@author: t1
"""

def pattern2number(pattern):
    '''
    maps pattern to alphabetical position of pattern from 4**k patterns
    '''
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
    '''
    maps numbers to kmers
    number -> alphabetical position from 4**k paterns
    k -> length of pattern
    '''
    
    dna_list = ['A','C','G','T']
    pat = ''
    for i in range(k-1,-1,-1):
        idx = int(number/4**(i))
        number = number % (4**i)
        pat += dna_list[idx]
        
    return pat

print(number2pattern(5437, 8))