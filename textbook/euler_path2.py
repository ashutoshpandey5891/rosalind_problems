#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 13:50:09 2021

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
        
# file_path = 'sample_data/euler_path2.txt'
# file_path = 'test_data/dataset_203_6.txt'
file_path = 'test_data/rosalind_ba3g.txt'
in_nodes,out_nodes = read_file(file_path)

path = get_euler_path(in_nodes, out_nodes)
print('->'.join(path))