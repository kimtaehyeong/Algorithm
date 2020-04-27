# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:26:30 2020

@author: Taehyung
"""

N = int(input())
a = []
for i in range(N):
    b = int(input())
    a.append(b)
a.sort()
for i in a:
    print(i)