#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 12:23:37 2021

@author: t1
"""

import time
import random
from itertools import product

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.clock()
        result = func(*args,**kwargs)
        end = time.clock()
        print(' {} executed in time : {:.6f} sec'.format(func.__name__,end - start))
        return result
    return wrapper

def read_file(file_path):
    k = None
    with open(file_path) as f:
        lines = f.readlines()
        k = int(lines[0].strip())
    return k

def get_binary_strings(k):
    bin_list = list(product(*[['0','1']]*k))
    bin_list_str = [''.join(list(el)) for el in bin_list]
    return bin_list_str

def get_composition(dna_string,k):
    comp_list = []
    for i in range(len(dna_string)-k+1):
        comp_list.append(dna_string[i:(i+k)])
    return comp_list


def get_debrujin(pattern_lst):
    # pattern_lst = get_composition(dna_string, k)
    key_list = []
    val_list = []
    for pattern in pattern_lst:
        pres = pattern[:-1]
        suff = pattern[1:]
        if pres not in key_list:   
            key_list.append(pres)
            val_list.append([suff])
        else:
            idx = key_list.index(pres)
            val_list[idx].append(suff)
    return key_list,val_list

def get_euler_cycle(in_nodes,out_nodes):

    edges_dict = {in_:out_ for in_,out_ in zip(in_nodes,out_nodes)}
    unused_nodes = []
    cycle = []
    
    ## cycle 0
    node1 = random.choice(in_nodes)
    node2 = ''
    while True:        
        cycle.append(node1)
        if (node1 not in edges_dict):
            break
        target_node_list = edges_dict[node1]
        if len(target_node_list) > 1:
            node2 = target_node_list[0]
            target_node_list = target_node_list[1:]
            edges_dict[node1] = target_node_list
            unused_nodes.append(node1)
        else:
            node2 = target_node_list[0]
            _ = edges_dict.pop(node1)
            if node2 in unused_nodes:
                idx = unused_nodes.index(node2)
                unused_nodes = unused_nodes[:idx] + unused_nodes[(idx+1):]
        node1 = node2
        node2 = ''
    
    # print(len(edges_dict))
    # print(unused_nodes)
    count = len(edges_dict)
    
    while count > 0:  
        unused_nodes = [node for node in cycle if node in edges_dict]
        node1 = random.choice(unused_nodes)
        temp_idx = cycle.index(node1)
        temp_cycle = cycle[temp_idx:-1] + cycle[:temp_idx]
        
        while True:
            node2 = ''
            temp_cycle.append(node1)
            if (node1 not in edges_dict):
                break
            
            target_node_list = edges_dict[node1]
            if len(target_node_list) > 1:
                node2 = target_node_list[0]
                target_node_list = target_node_list[1:]
                edges_dict[node1] = target_node_list
            else:
                node2 = target_node_list[0]
                _ = edges_dict.pop(node1)
            node1 = node2
            node2 = ''
        
        count = len(edges_dict)
        cycle = temp_cycle
        # print(edges_dict)
        # print('count : ',count)
        # print('cycle len : ',len(cycle))
        # print(unused_nodes)
        
    return cycle

def path2genome(genome_path):
    genome_str = genome_path[0]
    genome_str = genome_str + ''.join([s[-1] for s in genome_path[1:]])
    return genome_str



# file_path = 'sample_data/uni_circle_string_k.txt'
file_path = 'test_data/rosalind_ba3i.txt'
k = read_file(file_path)
# k=5
bin_list = get_binary_strings(k)
key_list,val_list = get_debrujin(bin_list)
path = get_euler_cycle(key_list,val_list)
# print('->'.join(path))
bin_string = path2genome(path)
print(bin_string[:-(k-1)])