#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 11:25:51 2021

@author: t1
"""
import random
import time

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
    kmer_list = []
    with open(file_path) as f:
        lines = f.readlines()
        k = int(lines[0].strip())
        for line in lines[1:]:
            kmer_list.append(line.strip())
    return k,kmer_list

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

def path2genome(genome_path):
    genome_str = genome_path[0]
    genome_str = genome_str + ''.join([s[-1] for s in genome_path[1:]])
    return genome_str

# @time_it
def get_kmer2genome(pattern_lst):
    key_list,val_list = get_debrujin(pattern_lst)
    path = get_euler_path(key_list,val_list)
    genome = path2genome(path)
    return genome

def check_compos(pattern_lst,k,genome):
    genome_comp = get_composition(genome, k)
    genome_sorted = sorted(genome_comp)
    sorted_pattern_lst = sorted(pattern_lst)
    if sorted_pattern_lst == genome_sorted:
        print('result verified')
    else:
        print('wrong result')

# file_path = 'sample_data/string_recons2.txt'
# file_path = 'test_data/dataset_203_7.txt'
file_path = 'test_data/rosalind_ba3h.txt'
k,pattern_lst = read_file(file_path)
genome = get_kmer2genome(pattern_lst)
print(genome)
# check_compos(pattern_lst, k, genome)