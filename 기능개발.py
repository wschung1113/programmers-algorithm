# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 17:36:26 2022

@author: Wonseok
"""

# 나의 답변
def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:
        progresses = [sum(x) for x in zip(progresses, speeds)]
        print(progresses)
        n_release = 0
        while True:
            
            if progresses[0] >= 100:
                n_release += 1
                progresses.pop(0)
                speeds.pop(0)
                if len(progresses) == 0:
                    break
            else:
                break
        if n_release > 0:
            answer.append(n_release)
        
        
            
            
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))















































