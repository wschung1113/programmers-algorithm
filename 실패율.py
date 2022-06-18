# -*- coding: utf-8 -*-
"""
Created on Thu May 26 00:01:19 2022

@author: Wonseok
"""
# 내 풀이
# test 22 : 5216
def solution(N, stages):
    answer_dict = {}
        
    for i in range(1, N+1):
        loi = [s for s in stages if s >= i]
        n_dodal = len(loi)
        if n_dodal == 0:
            answer_dict[i] = 0
        else:
            n_stuck = len([lo for lo in loi if lo == i])
            answer_dict[i] = n_stuck / n_dodal
        
    answer_dict = {k: v for k, v in sorted(answer_dict.items(), key=lambda item: item[1], reverse=True)}
        
    answer = list(answer_dict.keys())
        
        
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
    
# 더 빠른 풀이
def solution(N, stages):
    answer_dict = {}
    for i in range(1, N+1):
        if i == 1:
            prev_n_dodal, prev_n_stuck = 0, 0
            n_dodal = len(stages) # stages consists of elements greater than 1
            n_stuck = len([s for s in stages if s == 1])
        else:
            n_stuck = len([s for s in stages if s == i])
            n_dodal = prev_n_dodal - prev_n_stuck
        
        if n_dodal == 0:
            answer_dict[i] = 0
        else:
            answer_dict[i] = n_stuck / n_dodal
        
        prev_n_dodal = n_dodal
        prev_n_stuck = n_stuck
        
    answer_dict = {k: v for k, v in sorted(answer_dict.items(), key=lambda item: item[1], reverse=True)}
        
    answer = list(answer_dict.keys())
    
    return answer
    
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))

# 다른 사람 풀이
def solution(N, stages):
    fail_perc = []
    for _ in range(1, N + 1):
        # print(_)
        denom = 0
        numer = 0
        for stage in stages:
            if stage >= _:
                denom += 1
            if stage == _:
                numer += 1
        try:
            fail_perc.append((_, numer / float(denom)))
        except:
            fail_perc.append((_, 0))
    fail_perc.sort(key=lambda x: x[1], reverse=True)
    return [_[0] for _ in fail_perc]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))