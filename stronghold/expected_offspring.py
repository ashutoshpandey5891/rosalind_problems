#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:03:04 2020

@author: t1
"""

def expected_offspring(a,b,c,d,e,f):

    '''
    Function calculates expected offspring who display dominant phenotype,
    for a population with couples with 6 different genotypes
    
    problem statement : http://rosalind.info/problems/iev/
    '''
        
    return (2*a + 2*b + 2*c + 1.5*d + e + 0*f)

print(expected_offspring(17319,19002,16840,17461,16317,18128))