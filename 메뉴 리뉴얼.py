# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 20:32:41 2022

@author: Wonseok
"""

# 나의 답변
def solution(orders, course):
    answer = []
    
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))

max(set(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]), key = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"].count)
list(combinations(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]))

def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c+[a[0]]]
    return cs

print(combs(''.join("ABCDE")))
