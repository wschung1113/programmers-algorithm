# -*- coding: utf-8 -*-
"""
Created on Wed May 25 15:06:03 2022

@author: Wonseok
"""
# 나의 풀이
def solution(array, commands):
    answer = []
    
    for c in commands:
        # print(c[0])
        # print(c[1])
        sub_list = array[(c[0]-1):(c[1])]
        # print(sub_list)
        sub_list.sort()
        # print(sub_list)
        # print(sub_list_sorted)
        # print(sub_list_sorted[c[2]-1])
        answer.append(sub_list[c[2]-1])
    
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))