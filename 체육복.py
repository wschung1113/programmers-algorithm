# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:32:30 2022

@author: Wonseok
"""

def solution(n, lost, reserve):
    answer = 0
    
    lost.sort()
    reserve.sort()
    
    true_reserve = [x for x in reserve if x not in lost]
    
    answer += len(reserve) - len(true_reserve)
    
    true_lost = [x for x in lost if x not in reserve]
    
    for lo in true_lost:
        if lo - 1 in true_reserve:
            answer += 1
            true_reserve.remove(lo-1)
        elif lo + 1 in true_reserve:
            answer += 1
            true_reserve.remove(lo+1)
            
    
    answer = answer + (n - len(lost))
    
    
    return answer