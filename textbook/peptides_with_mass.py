#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:29:48 2021

@author: t1
"""

from itertools import product
from collections import Counter
import pickle

import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.clock()
        result = func(*args,**kwargs)
        end = time.clock()
        print(' {} executed in time : {:.6f} sec'.format(func.__name__,end - start))
        return result
    return wrapper

MOLE_MASS = {
    'G' : 57,'A':71,'S':87,'P':97,'V':99,'T':101,
    'C' : 103,'I':113,'L':113,'N':114,'D':115,'K':128,
    'Q' : 128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186
    }

mass_list = list(set(MOLE_MASS.values()))

def read_file(file_path):
    pep_mass = None
    with open(file_path) as f:
        pep_mass = int(f.read().strip())
    return pep_mass

def get_n_masses(n):
    n_combin = list(product(*[mass_list]*n))
    masses = []
    for comb in n_combin:
        masses.append(sum(comb))
    return masses

@time_it
def get_n_peps(pep_mass,min_n,max_n):
    mass_count = 0
    for n in range(min_n,max_n):
        n_masses = get_n_masses(n)
        for mass in n_masses:
            if mass == pep_mass:
                mass_count+=1
    return mass_count

# pep_mass = 1024
# min_n = 1
# max_n = 8
# mass_count = get_n_peps(pep_mass,min_n,max_n)
# print(mass_count)
