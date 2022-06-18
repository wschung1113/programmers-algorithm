# -*- coding: utf-8 -*-
"""
Created on Fri May 27 00:25:13 2022

@author: Wonseok
"""

# 나의 풀이
def solution(a, b):
    
    num_days = b
    for month in range(a):
        if month == 0:
            continue
        elif month == 1:
            num_days += 31
        elif month == 2:
            num_days += 29
        elif month == 3:
            num_days += 31
        elif month == 4:
            num_days += 30
        elif month == 5:
            num_days += 31
        elif month == 6:
            num_days += 30
        elif month == 7:
            num_days += 31
        elif month == 8:
            num_days += 31
        elif month == 9:
            num_days += 30
        elif month == 10:
            num_days += 31
        elif month == 11:
            num_days += 30
    
    remainder = num_days % 7
    # print(num_days)
    # print(remainder)
    answer = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU'][remainder-1]
    
    return answer

print(solution(5, 24))