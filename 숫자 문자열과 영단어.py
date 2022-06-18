# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:14:14 2022

@author: Wonseok
"""
s = "one4seveneight"
def solution(s):
    if s.isdigit():
        return int(s)
    answer = ''
    tmp_word = ''
    eng_nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    nums = list(range(10))
    for c in s:
        if c.isdigit():
            answer += c
            continue
        else:
            tmp_word += c
        if tmp_word in eng_nums:
            answer += str(nums[eng_nums.index(tmp_word)])
            tmp_word = ''
        
        
    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
