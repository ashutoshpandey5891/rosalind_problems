#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:19:43 2020

@author: t1
"""

def get_offspring_prob(k,m,n,dominant = True):
    if dominant:
        return 1.0 - (n*(n-1.0) + m*n + m*(m-1)/4)/((k+m+n)*(k+m+n-1.0))
    else:
        return (n*(n-1.0) + m*n + m*(m-1)/4)/((k+m+n)*(k+m+n-1.0))
    
    
if __name__ == '__main__':
    print(get_offspring_prob(22,15,18))