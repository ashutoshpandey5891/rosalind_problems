#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 00:07:24 2020

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

with open('test_data/Vibrio_cholerae.txt') as f:
    dna_seq = f.read()
    
pattern = 'CTTGATCAT'

@time_it
def get_start_pos(dna_seq,pat):
    start_pos = []
    for i in range(len(dna_seq)-len(pat)+1):
        if dna_seq[i:(i+len(pat))] == pat : 
            start_pos.append(i)
    return start_pos


start_pos = get_start_pos(dna_seq, pattern)
print(' '.join([str(i) for i in start_pos]))