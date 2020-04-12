# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:08:11 2020

@author: Taehyung
"""

# https://www.acmicpc.net/problem/2920

a = list(map(int, input().split()))

ascend = 0
descend = 0

for i in range(1, 8):
    if a[i] > a[i-1]:
        ascend = 1
    elif a[i] < a[i-1]:
        descend = 1


if ascend == 1 and descend == 1:
    print('mixed')
elif ascend == 1 and descend == 0:
    print('ascending')
elif ascend == 0 and descend == 1:
    print('descending')
    