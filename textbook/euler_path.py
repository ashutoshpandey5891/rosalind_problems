#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 10:45:03 2021
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
    path_ = []
    
    node1 = start_node
    node2 = ''
    while True:
        path_.append(node1)
        if node1 not in edges_dict.keys():
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
    
    cycle = path_[1:-1] + [path_[1]]
    count = len(edges_dict)
    cycle_start_node = path_[1]
    cycle_end_node = path_[-2]
    # print(path_)
    # print(cycle)
    # print(count)
    while count > 0:  
        unused_nodes = [node for node in cycle if node in edges_dict]
        node1 = random.choice(unused_nodes)
        temp_idx = cycle.index(node1)
        temp_cycle = cycle[temp_idx:-1] + cycle[:temp_idx]
        # print(unused_nodes)
        
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
    cycle = cycle[:-1]
    start_idxs = [idx for idx,node in enumerate(cycle) if node == cycle_start_node]
    for idx2 in start_idxs:
        temp_path = cycle[idx2:] + cycle[:idx2]
        if temp_path[-1] == cycle_end_node:
            cycle = temp_path[:]
            # print(cycle)
    path_ = [path_[0]] + cycle[:] + [path_[-1]]
    return path_
        

file_path = 'sample_data/euler_path.txt'
# file_path = 'test_data/dataset_203_6.txt'
in_nodes,out_nodes = read_file(file_path)

path = get_euler_path(in_nodes, out_nodes)
print('->'.join(path))
