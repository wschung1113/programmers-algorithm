# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 23:40:05 2022

@author: Wonseok
"""

# 나의 풀이
def solution(s):
    answer = ''
    lower_case_letters = sorted([c for c in s if c.islower()], reverse=True)
    upper_case_letters = sorted([c for c in s if c.isupper()], reverse=True)
    for _ in range(len(lower_case_letters)+len(upper_case_letters)):
        answer += (lower_case_letters + upper_case_letters)[_]
    return answer

# 다른 사람의 풀이
def solution(s):
    return ''.join(sorted(s, reverse=True))

print(solution("Zbcdefg"))