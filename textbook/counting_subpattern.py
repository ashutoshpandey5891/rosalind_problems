#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:59:21 2020

@author: t1
"""

def read_file(file_path):
    with open(file_path,'r') as f:
        lines = f.readlines()
        
    text = lines[0].strip()
    pattern = lines[1].strip()
    
    return text,pattern


def count(text,pattern):
    cnt = 0
    for i in range(len(text)-len(pattern)+1):
        subtext = text[i:(i+len(pattern))]  
        if subtext == pattern:
            cnt += 1
    return cnt


# file_path = 'sample_data/counting_patterns.txt'
file_path = 'test_data/dataset_2_7.txt'
text,pattern = read_file(file_path)
print(count(text,pattern))