#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:01:45 2020

@author: t1
"""

def read_file(file_path):
    with open(file_path,'r') as f:
        lines = f.readlines()
    n = int(lines[0].strip())
    adjac_list = []
    for i in range(1,len(lines)):
        line = lines[i].strip().split(' ')
        adjac_list.append((int(line[0]),int(line[1])))
    return n,adjac_list
    

# def get_tree(n,adjac_list):
#     node2n = {}
#     for adjac in adjac_list:
#         if not adjac[0] in node2n:
#             node2n[adjac[0]] = 1
#         else:
#             node2n[adjac[0]] += 1
            
#         if not adjac[1] in node2n:
#             node2n[adjac[1]] = 1
#         else:
#             node2n[adjac[1]] += 1
#     n2node = {}
#     for node,n in node2n.items():
#         if n in n2node:
#             n2node[n].append(node)
#         else:
#             n2node[n] = [node]
    
#     return node2n,n2node

def get_n_edges(n,adjac_list):
    n_act = len(adjac_list)
    if n_act < (n-1):
        return (n-1) - n_act
    else:
        return 0
    
# file_path = 'sample_data/completing_tree.txt'
file_path = 'test_data/rosalind_tree.txt'
n,adjac_list = read_file(file_path)
# node2n,n2node = get_tree(n, adjac_list)
print(get_n_edges(n, adjac_list))