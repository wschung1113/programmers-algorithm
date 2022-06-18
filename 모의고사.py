# -*- coding: utf-8 -*-
"""
Created on Wed May 25 16:57:52 2022

@author: Wonseok
"""

# 나의 풀이
def solution(answers):
    answer = []
    format_1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    format_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    format_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # while True:
    #     count_1 = 1
    #     count_2 = 1
        
    #     if 10*count_1 >= len(answers):
    #         remain_1 = 10*count_1 - len(answers)
    #     else:
    #         count_1 += 1
        
    #     if 8*count_2 >= len(answers):
    #         remain_2 = 8*count_2 - len(answers)
    #     else:
    #         count_2 += 1
            
    #     if 10*count_1 >= len(answers) and 8*count_2 >= len(answers):
    #         break
        
    # answers_1 = format_1*(count_1-1) + format_1[:-remain_1]
    # answers_2 = format_2*(count_2-1) + format_2[:-remain_2]
    # answers_3 = format_3*(count_1-1) + format_3[:-remain_1]
        
    # print(answers_1)
    # print(answers_2)
    # print(answers_3)    
    
    formats = [format_1*1000, format_2*1250, format_3*1000]
    
    
    score_1 = 0
    score_2 = 0
    score_3 = 0
    
    for i, a in enumerate(answers):
        # print(answers_1)
        # print(answers_1 == a)
        if formats[0][i] == a:
            score_1 += 1
            
        if formats[1][i] == a:
            score_2 += 1
            
        if formats[2][i] == a:
            score_3 += 1
    
    scores = [score_1, score_2, score_3]
    max_score = max(scores)
    
    # answer = [scores.index(x) + 1 for x in scores if x == max_score]
    for i, s in enumerate(scores):
        if s == max_score:
            answer.append(i+1)
    
    
    
    print(max_score)    
    # print(answer)
    
        
    answer.sort()    
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
