# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 22:44:11 2022

@author: Wonseok
"""

def solution(s):
    if len(s) % 2:
        answer = s[len(s)-(len(s)//2)-1]
    else:
        answer = s[((len(s)//2)-1):((len(s)//2)+1)]
    
    return answer

print(solution('abcde'))