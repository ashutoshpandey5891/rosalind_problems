#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 13:28:06 2020

@author: t1
"""

from itertools import permutations

n = 6
tmp_list = list(range(1,(n+1)))
perms = list(permutations(tmp_list,len(tmp_list)))

print(len(perms))
for p in perms:
    print(' '.join([str(i) for i in p]))