# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 17:56:26 2022

@author: Wonseok
"""

# 나의 답변
# def solution(numbers, target):
#     sums = []
#     for idx, n in enumerate(numbers):
#         # print(sums)
#         if len(sums) == 0:
#             sums.append(n)
#             sums.append(-n)
#         else:
#             to_add = []
#             for i in range(2**idx):
#                 to_add.append(sums[-(i+1)]+n)
#                 to_add.append(sums[-(i+1)]+-n)
#             sums += to_add
#     # print(sums)
#     # return sums
#     sums = sums[-len(to_add):]
#     print(sums)
#     answer = len([x for x in sums if x == target])
#     # print(answer)
#     return answer
#
# print(solution([1, 1, 1], 3))
# print(solution([1, 1, 1, 1, 1], 3))
# print(solution([4, 1, 2, 1], 4))

# 다른 사람의 풀이 1
# DFS
# numbers = [1, 1, 1]
# target = 3

# numbers = [1, 1]
# target = 2
# target = 4

# numbers = [1]
# target = 1
# target = 3
# target = 3
# target = 5

# numbers = [] # list가 empty list가 되면 종단 조건
# target = 0
# def solution(numbers, target):
#     if not numbers and target == 0 : # not list는 list가 empty이면 True를 반환
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# 다른 사람의 풀이 2
# from itertools import product
#
# numbers = [1, 1, 1]
# target = 3
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)

print(solution([1, 1, 1], 3))
print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))