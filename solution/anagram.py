# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:35:42 2019

@author: kimta
"""

# 애나그램(anagram)은 문장 또는 단어의 철자 순서를 바꾸는 놀이를 말한다.
word1 = 'samsung'
word2 = 'smsaugn'

# python dict 이용

from collections import Counter

def anagram(s1, s2): #counter 이용
    counter = Counter()
    for c in s1:
        counter[c]+=1
    for c in s2:
        counter[c]-=1
    
    for i in counter.values():
        if i:
            return False
    return True
print(anagram(word1, word2)) #True


#해시 함수 속성 이용
import string

def hash_func(astring):
    s = 0
    for one in astring:
        if one in string.whitespace:
            continue
        s = s + ord(one)
    return s

def anagram_hash_func_find(word1, word2):
    return hash_func(word1) == hash_func(word2)

print(anagram_hash_func_find(word1, word2) is True) #True