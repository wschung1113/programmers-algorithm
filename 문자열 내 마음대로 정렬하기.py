# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 23:02:22 2022

@author: Wonseok
"""

# 내 방법
def solution(strings, n):
    answer = []
    if len(strings) == 1:
        return strings
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for a in alphabets:
        # print(a)
        tmp_list = [words for words in strings if words[n] == a]
        # print(tmp_list)
        if len(tmp_list) == 0:
            continue
        elif len(tmp_list) == 1:
            answer += tmp_list
        else:
            tmp_list.sort()
            answer += tmp_list
    
    return answer

# 다른 사람 방법
def solution(strings, n):
    # return sorted(strings, key=lambda x: x[n])
    return sorted(strings, key=lambda str: (str[n], str))

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))
