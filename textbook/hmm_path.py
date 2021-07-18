#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:39:35 2020

@author: t1
"""
import numpy as np

path = 'AABBBAABABAAAABBBBAABBABABBBAABBAAAABABAABBABABBAB'
path2 = 'BBABBBABBAABABABBBAABBBBAAABABABAAAABBBBBAABBABABB'
path3 = 'BABBBBBAAABAAABBBBAABBBBBBAABBBBBBBBABBBBBBABBBAAB'

prob_mat = np.array([[0.194,0.806],[0.273,0.727]])
prob_mat2 = np.array([[0.863,0.137],[0.511,0.489]])
prob_mat3 = np.array([[0.423,0.577],[0.64,0.36]])

def get_path_prob(path,prob_mat):
    print(prob_mat2)
    
    total_prob = 0.5
    for i in range(1,len(path)):
        l2i = {'A':0,'B':1}
        prev_l = l2i[path[i-1]]
        current_l = l2i[path[i]]
        total_prob *= prob_mat[prev_l,current_l]
        
    return total_prob

print(get_path_prob(path3, prob_mat3))
    
    