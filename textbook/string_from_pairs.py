#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:14:54 2021

@author: t1
"""

import time
import random

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
    d = None
    read_pairs = []
    with open(file_path) as f:
        lines = f.readlines()
        k,d = lines[0].strip().split(' ')
        k = int(k.strip())
        d = int(d.strip())
        for line in lines[1:]:
            read_pairs.append(line.strip())
    return read_pairs,k,d

def get_debrujin(pattern_lst):
    # pattern_lst = get_composition(dna_string, k)
    key_list = []
    val_list = []
    for pattern in pattern_lst:
        # pres = pattern[:-1]
        # suff = pattern[1:]
        p1,p2 = pattern.split('|')
        pres = '{}|{}'.format(p1[:-1],p2[:-1])
        suff = '{}|{}'.format(p1[1:],p2[1:])
        # print(pres,suff)
        if pres not in key_list:   
            key_list.append(pres)
            val_list.append([suff])
        else:
            idx = key_list.index(pres)
            val_list[idx].append(suff)
    return key_list,val_list

def get_euler_path(in_nodes,out_nodes):
    edges_dict = {in_:out_ for in_,out_ in zip(in_nodes,out_nodes)}
    tmp = [elem1 for elem in out_nodes for elem1 in elem]
    all_nodes = list(set(in_nodes + tmp))
    start_node = ''
    end_node = ''
    for node in all_nodes:
        in_count = tmp.count(node)
        out_count = len(edges_dict.get(node,[]))
        if out_count > in_count:
            # print('start node found : {}'.format(node))
            start_node = node
        if out_count < in_count:
            # print('end node found : {}'.format(node))
            end_node = node
    
    ## add one node from end node to start node
    end_node_list = edges_dict.get(end_node,[])
    end_node_list.append(start_node)
    edges_dict[end_node] = end_node_list
    # print(edges_dict)
    ## find the euler cycle
    cycle = []
    node1 = start_node
    node2 = ''
    while True:        
        cycle.append(node1)
        if (node1 not in edges_dict):
            break
        
        target_node_list = edges_dict[node1]
        # print(node1)
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
    start_node_idxs = [idx for idx,node in enumerate(cycle) if node == start_node]
    path = []
    for idx in start_node_idxs:
        temp_path = cycle[idx:-1] + cycle[:idx]
        if temp_path[-1] == end_node:
            path = temp_path
    return path

def get_string_form_pairs_path(read_pairs,k,d):
    pref,suff = read_pairs[0].split('|')
    pref_string = pref
    suff_string = suff
    for pair in read_pairs[1:]:
        pref,suff = pair.split('|')
        pref_string += pref[-1]
        suff_string += suff[-1]
    dna_string = pref_string + suff_string[-(k+d):]
    return dna_string

@time_it
def kmer_pair2genome(read_pairs,k,d):
    in_nodes,out_nodes = get_debrujin(read_pairs)
    euler_path = get_euler_path(in_nodes, out_nodes)
    genome_string = get_string_form_pairs_path(euler_path, k, d)
    return genome_string

# file_path = 'sample_data/string_from_pairs.txt'
file_path = 'test_data/rosalind_ba3j.txt'
read_pairs,k,d = read_file(file_path)
genome_string = kmer_pair2genome(read_pairs, k, d)
print(genome_string)
