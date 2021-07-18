#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:30:02 2020

@author: t1
"""


import time
# from temp_string_composition import run

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.clock()
        result = func(*args,**kwargs)
        end = time.clock()
        print(' {} executed in time : {:.6f} sec'.format(func.__name__,end - start))
        return result
    return wrapper

def read_file(file_path):
    genome_path = []
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            genome_path.append(line.strip())
    return genome_path


def path2genome(genome_path):
    genome_str = genome_path[0]
    genome_str = genome_str + ''.join([s[-1] for s in genome_path[1:]])
    return genome_str

# file_path = 'sample_data/path2genome.txt'
# file_path = 'test_data/dataset_198_3.txt'
file_path = 'test_data/rosalind_ba3b.txt'
genome_path = read_file(file_path)
genome = path2genome(genome_path)
print(genome)
