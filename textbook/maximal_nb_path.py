#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 14:32:33 2021

@author: t1
"""
import random

def read_file(file_path):
    in_nodes = []
    out_nodes = []
    with open(file_path) as f:
        for line in f.readlines():
            line = line.strip().split(' -> ')
            in_ = line[0]
            in_nodes.append(in_.strip())
            out = line[1].strip().split(',')
            out_nodes.append([s.strip() for s in out])
    return in_nodes,out_nodes

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

def get_count(node,edges_dict):
    temp_list = [elem1 for elem in edges_dict.values() for elem1 in elem]
    in_count = temp_list.count(node)
    out_count = len(edges_dict.get(node,[]))
    return in_count,out_count

def get_contigs(in_nodes,out_nodes):
    edges_dict = {in_:out_ for in_,out_ in zip(in_nodes,out_nodes)}
    tmp = [elem1 for elem in out_nodes for elem1 in elem]
    all_nodes = list(set(in_nodes + tmp))
    
    node1 = ''
    node2 = ''
    all_nb_paths = []
    nb_path = []
    # select unbalanced node 
    unbal_nodes = []
    for node in all_nodes:
        in_count,out_count = get_count(node,edges_dict)
        if in_count == 1 and out_count == 1:
            continue
        else:
            unbal_nodes.append(node)
    counter = 0
    while counter < len(unbal_nodes):
        node1 = unbal_nodes[counter]
        if node1 in edges_dict:
            nb_path = [node1]
            out_nodes_list = edges_dict.get(node1)
            if len(out_nodes_list) > 1:
                node2 = out_nodes_list[0]
                out_nodes_list = out_nodes_list[1:]
                edges_dict[node1] = out_nodes_list
            else:
                node2 = out_nodes_list[0]
                _ = edges_dict.pop(node1)
            node1 = node2
            node2 = ''
            nb_path.append(node1)
            while node1 not in unbal_nodes:
                node2 = edges_dict[node1][0]
                _ = edges_dict.pop(node1)
                node1 = node2
                node2 = ''
                nb_path.append(node1)
            all_nb_paths.append(nb_path)
            nb_path = []
        else:
            counter += 1
    
    iso_cycles = []
    while len(edges_dict) > 0:
        node1 = random.choice(list(edges_dict.keys()))
        cycle = [node1]
        while node1 in edges_dict:
            node2 = edges_dict[node1][0]
            _ = edges_dict.pop(node1)
            node1 = node2
            node2 = ''
            cycle.append(node1)
        iso_cycles.append(cycle)
    
    return all_nb_paths + iso_cycles

# file_path = 'sample_data/maximal_nb_path.txt'
file_path = 'test_data/rosalind_ba3m.txt'
in_nodes,out_nodes = read_file(file_path)
all_paths = get_contigs(in_nodes, out_nodes)
for path in all_paths:
    print(' -> '.join(path))