#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 13:24:50 2021

@author: t1
"""

import time
import numpy as np

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.clock()
        result = func(*args,**kwargs)
        end = time.clock()
        print(' {} executed in time : {:.6f} sec'.format(func.__name__,end - start))
        return result
    return wrapper

def read_file(file_path):
    spectrum = None
    with open(file_path) as f:
        lines = f.readlines()
        spectrum = [int(x) for x in lines[0].strip().split(' ')]
    return spectrum

@time_it
def get_convolution1(spectrum):
    '''
    spectrum -> list of ints
    '''
    sorted_spectrum = sorted(spectrum)
    conv_list = []
    for idx1 in range(len(spectrum) - 1):
        for idx2 in range((idx1+1),len(spectrum)):
            conv = sorted_spectrum[idx2] - sorted_spectrum[idx1]
            if conv > 0:
                conv_list.append(conv)
    # sorted_conv = sorted(conv_list)
    return conv_list


def get_convolution2(spectrum):
    '''
    spectrum -> list of ints
    '''
    spec_arr = np.array(spectrum)
    conv_mat = spec_arr.reshape(-1,1) - spec_arr.reshape(1,-1)
    conv_list = list(conv_mat[conv_mat > 0].ravel())
    return conv_list

# file_path = 'sample_data/spectrum_convolution.txt'
file_path = 'test_data/rosalind_ba4h.txt'
spectrum = read_file(file_path)
# conv_list1 = get_convolution1(spectrum)
conv_list2 = get_convolution2(spectrum)
# print('conv method 1 : \n'+' '.join([str(x) for x in conv_list1]))
print(' '.join([str(x) for x in conv_list2]))