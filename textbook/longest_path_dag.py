#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 10:02:31 2021

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
    start_node = None
    end_node = None
    in_nodes = []
    out_nodes = []
    edge_weights = []
    with open(file_path) as f:
        lines = f.readlines()
        start_node = int(lines[0].strip())
        end_node = int(lines[1].strip())
        for line in lines[2:]:
            line = line.strip().split('->')
            in_node,[out_node,weight] = line[0],line[1].split(':')
            in_nodes.append(int(in_node))
            out_nodes.append(int(out_node))
            edge_weights.append(int(weight))
    return start_node,end_node,in_nodes,out_nodes,edge_weights

def get_max_weight(node,in_nodes,out_nodes,edge_weights,path_length_dict):
    max_weight = 0
    max_weight_node = None
    for i,out_node in enumerate(out_nodes):
        if node == out_node:
            
            if (edge_weights[i]+path_length_dict.get(in_nodes[i],0))> max_weight:
                max_weight = edge_weights[i]+path_length_dict.get(in_nodes[i],0)
                max_weight_node = in_nodes[i]
    return max_weight,max_weight_node

def get_longest_path(start_node,end_node,in_nodes,out_nodes,edge_weights):
    path_dict = {}
    path_length_dict = {start_node:0}
    
    zero_indegree_list = [node for node in in_nodes if node not in out_nodes]
    
    while len(set(zero_indegree_list)) > 1:
        
        in_nodes_new = []
        out_nodes_new = []
        edge_weights_new = []
        
        for i,node in enumerate(in_nodes):
            if (node not in out_nodes) and (node != start_node):
                # print(node,'->',out_nodes[i])
                continue
            else:
                in_nodes_new.append(node)
                out_nodes_new.append(out_nodes[i])
                edge_weights_new.append(edge_weights[i])
                
        in_nodes = in_nodes_new[:]
        out_nodes = out_nodes_new[:]
        edge_weights = edge_weights_new[:]
        
        zero_indegree_list = [node for node in in_nodes if node not in out_nodes]
        # print(zero_indegree_list)
        
    for node in range(start_node+1,end_node+1):
        max_weight,max_weight_node = get_max_weight(node, in_nodes, out_nodes, edge_weights, path_length_dict)
        if max_weight_node != None:
            path_length_dict[node] = max_weight
            path_dict[node] = max_weight_node
    max_length = path_length_dict[end_node]
    # print(max_length)
    longest_path = []
    node = end_node
    # print(path_length_dict)
    while node != start_node:
        longest_path.insert(0,node)
        # print(node)
        node = path_dict[node]
    longest_path.insert(0,start_node)
    return max_length,longest_path


# file_path = 'sample_data/longest_path_dag2.txt'
file_path = 'test_data/dataset_245_7.txt'
start_node,end_node,in_nodes,out_nodes,edge_weights = read_file(file_path)
max_length,longest_path = get_longest_path(start_node, end_node, in_nodes, out_nodes, edge_weights)
print(max_length)
print('->'.join([str(x) for x in longest_path]))
