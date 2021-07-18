#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 11:21:46 2020

@author: t1
"""
import random
import numpy as np

def read_file(file_path):
    in_nodes = []
    out_nodes = []
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            in_,out_ = line.strip().split('->')
            in_nodes.append(in_.strip())
            out_nodes.append([node.strip() for node in out_.strip().split(',')])
    return in_nodes,out_nodes

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
        
    # while len(edges_dict) > 0:
        
    
    

# file_path = 'sample_data/euler_cycle.txt'
file_path = 'test_data/rosalind_ba3f.txt'
in_nodes,out_nodes = read_file(file_path)
# edges_dict = {in_:out_ for in_,out_ in zip(in_nodes,out_nodes)}
# for in_,out_ in zip(in_nodes,out_nodes):
#     print(f'{in_} -> {out_}')
cycle = get_euler_cycle(in_nodes, out_nodes)
print('->'.join(cycle))