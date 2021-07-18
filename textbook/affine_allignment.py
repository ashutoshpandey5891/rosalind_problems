#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 11:46:21 2021

@author: t1
"""

import time
import numpy as np
np.set_printoptions(suppress = True)

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.clock()
        result = func(*args,**kwargs)
        end = time.clock()
        print(' {} executed in time : {:.6f} sec'.format(func.__name__,end - start))
        return result
    return wrapper

def read_file(file_path):
    str1 = None
    str2 = None
    with open(file_path) as f:
        lines = f.readlines()
        str1 = lines[0].strip()
        str2 = lines[1].strip()
    return str1,str2

def read_score_mat(file_path):
    score_mat = None
    letter2idx = {}
    with open(file_path) as f:
        lines = f.readlines()
        letter_line = lines[0].strip().split()
        n = len(letter_line)
        score_mat = np.zeros((n,n))
        letter_count = 0
        for line in lines[1:]:
            line = line.strip().split()
            letter = line[0]
            assert letter == letter_line[letter_count] , "letters dont match!"
            score_mat[letter_count,:] = np.array(line[1:]).astype(int)
            letter2idx[letter] = letter_count 
            letter_count += 1
    return score_mat,letter2idx

def update_upper(i,j,upper_mat,middle_mat,gap_start_p,gap_extend_p):
    vals_list = [middle_mat[i,j-1] - gap_start_p,upper_mat[i,j-1] - gap_extend_p]
    max_arg = np.argmax(vals_list)
    upper_mat[i,j] = vals_list[max_arg]
    return upper_mat,max_arg

def update_lower(i,j,lower_mat,middle_mat,gap_start_p,gap_extend_p):
    vals_list = [middle_mat[i-1,j] - gap_start_p,-999999,lower_mat[i-1,j] - gap_extend_p]
    max_arg = np.argmax(vals_list)
    lower_mat[i,j] = vals_list[max_arg]
    return lower_mat,max_arg

def update_middle(i,j,lower_mat,upper_mat,middle_mat,str1,str2,score_mat,letter2idx):
    letter1_idx = letter2idx[str1[i-1]]
    letter2_idx = letter2idx[str2[j-1]]
    score_val = score_mat[letter1_idx,letter2_idx]
    vals_list = [middle_mat[i-1,j-1] + score_val,upper_mat[i,j],lower_mat[i,j]]
    max_arg = np.argmax(vals_list)
    middle_mat[i,j] = vals_list[max_arg]
    return middle_mat,max_arg

def update_backtrack(i,j,back_mid,back_up,back_low,uarg,larg,marg):
    # uarg -> value of upper mat max pos
    # larg -> value of lower mat max pos
    # marg -> value of middle mat max pos
    back_mid[i,j] = marg
    back_up[i,j] = uarg
    back_low[i,j] = larg
    return back_mid,back_up,back_low

def get_affine_allignment(str1,str2,score_mat,letter2idx,gap_start_p,gap_extend_p):
    len1 = len(str1)
    len2 = len(str2)
    
    ## initate matrices
    upper_mat = np.zeros((len1 + 1,len2 + 1))
    upper_mat[1:,0] = -9999
    upper_mat[0,1] = -gap_start_p
    for i in range(2,len2+1):
        upper_mat[0,i] = upper_mat[0,(i-1)] - gap_extend_p
    
    lower_mat = np.zeros((len1+1,len2+1))
    lower_mat[0,1:] = -9999
    lower_mat[1,0] = -gap_start_p
    for i in range(2,len1+1):
        lower_mat[i,0] = lower_mat[(i-1),0] - gap_extend_p
        
    middle_mat = np.zeros((len1+1,len2+1))
    middle_mat[0,1] = -gap_start_p
    middle_mat[1,0] = -gap_start_p
    for i in range(2,len1+1):
        middle_mat[i,0] = middle_mat[(i-1),0] - 1
    for i in range(2,len2+1):
        middle_mat[0,i] = middle_mat[0,(i-1)] - 1
    
    back_mid = np.zeros((len1+1,len2+1))
    back_up = np.zeros((len1+1,len2+1))
    back_low = np.zeros((len1+1,len2+1))
    
    for j in range(1,len2+1):
        for i in range(1,len1+1):
        
            upper_mat,uarg = update_upper(i, j, upper_mat, middle_mat, gap_start_p, gap_extend_p)
            lower_mat,larg = update_lower(i, j, lower_mat, middle_mat, gap_start_p, gap_extend_p)
            middle_mat,marg = update_middle(i, j, lower_mat, upper_mat, middle_mat, str1, str2, score_mat, letter2idx)
            back_mid,back_up,back_low = update_backtrack(i, j, back_mid,back_up,back_low, uarg, larg, marg)
    print(upper_mat)
    print("")
    # print(lower_mat)
    # print("")
    print(middle_mat)
    max_score = middle_mat[-1,-1]
    return back_mid,back_up,back_low,max_score
    
# def get_result_strings(str1,str2,back_mat,back_up,back_low):
#     res1 = ''
#     res2 = ''
#     i = len(str1)
#     j = len(str2)
#     val_list = []
#     val = None
#     while (i > 0) and (j > 0):
#         val = int(back_mat[i,j])
#         # print(back_val,back_up_val,back_low_val)
#         if val == 2:
#             # res2 += '-'
#             # res1 += str1[i-1]
#             i = i-1
#         elif val == 1:
#             # res2 += str2[j-1]
#             # res1 += '-'
#             j = j - 1
#         elif val == 0:
#             res2 += str2[j-1]
#             res1 += str1[i-1]
#             i -= 1
#             j -= 1
#         val_list.append(val)
        
#     idx = len(val_list) - 1

#     while (idx >= 0):
#         val = val_list[idx]
#         if val == 2:
#             res2 += '-'
#             res1 += str1[i-1]

#         elif val == 1:
#             res2 += str2[j-1]
#             res1 += '-'
            
#         elif val == 0:
#             res2 += str2[j-1]
#             res1 += str1[i-1]
#         idx -= 1
#     return res1,res2

def get_result_strings(str1,str2,back_mat,back_up,back_low):
    res1 = ''
    res2 = ''
    i = len(str1)
    j = len(str2)
    mats_list = [back_mat,back_up,back_low]
    graph = 0
    val = mats_list[int(graph)][i,j]
    if val == 2:
        res2 += '-'
        res1 += str1[i-1]
        i = i-1
    elif val == 1:
        res2 += str2[j-1]
        res1 += '-'
        j = j - 1
    elif val == 0:
        res2 += str2[j-1]
        res1 += str1[i-1]
        i -= 1
        j -= 1
    
    val = mats_list[int(graph)][i,j]
    while (i > 0) and (j > 0):
        if graph == 0:
            if val == 2:
                res2 += '-'
                res1 += str1[i-1]
                i = i-1
            elif val == 1:
                res2 += str2[j-1]
                res1 += '-'
                j = j - 1
            elif val == 0:
                res2 += str2[j-1]
                res1 += str1[i-1]
                i -= 1
                j -= 1
        else:
            if graph == 1:
                res2 += str2[j-1]
                res1 += '-'
                j = j - 1
            elif graph == 2:
                res2 += '-'
                res1 += str1[i-1]
                i = i-1
        graph = val
        val = mats_list[int(graph)][i,j]
    return res1,res2
        
        
            
score_mat_file_path = 'sample_data/BLOSUM62.txt'
score_mat,letter2idx = read_score_mat(score_mat_file_path)
gap_start_p = 11
gap_extend_p = 1

# file_path = 'sample_data/affine_allignment2.txt'
file_path = 'test_data/dataset_249_8.txt'
str1,str2 = read_file(file_path)

back_mat,back_up,back_low,max_score = get_affine_allignment(str2, str1, score_mat,letter2idx, gap_start_p, gap_extend_p)
res1,res2 = get_result_strings(str2, str1, back_mat,back_up,back_low)
print(int(max_score))
print(res2[::-1])
print(res1[::-1]) 