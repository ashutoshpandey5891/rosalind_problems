#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:50:45 2020

@author: t1
"""
import numpy as np
from scipy.special import comb

def get_prob(k,N):
    ''' 
    computes probability of at there bieng at least N AaBb organisms in kth generation
    probalem statement : http://rosalind.info/problems/lia/
    '''
    
    total_prob = 0.0
    # for i in range(N,2**k + 1):
    #     total_prob += (1/4)**i
        
    for i in range(N,2**k+1):
        total_prob += comb(2**k, i)*((1/4)**i * (3/4)**(2 ** k - i))
    return total_prob

# def get_n_from_k(k,n):
#     temp1 = np.prod(np.arange(1,k+1))
#     temp2 = np.prod(np.arange(1,n+1))
#     temp3 = np.prod(np.arange(1,k-n +1))
#     print(temp1,temp2,temp3)
#     return temp1/(temp2*temp3)

print(get_prob(7,32))