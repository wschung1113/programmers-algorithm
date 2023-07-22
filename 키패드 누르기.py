def find_distance(cur, dest):
    return abs(cur[0] - dest[0]) + abs(cur[1] - dest[1])

def solution(numbers, hand):
    answer = ""
    num_pad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]
    l_loc = (3, 0)
    r_loc = (3, 2)
    for n in numbers:
        if n in [1, 4, 7]:
            answer += "L"
            if n == 1:
                l_loc = (0, 0)
            elif n == 4:
                l_loc = (1, 0)
            elif n == 7:
                l_loc = (2, 0)
        elif n in [3, 6, 9]:
            answer += "R"
            if n == 3:
                r_loc = (0, 2)
            elif n == 6:
                r_loc = (1, 2)
            elif n == 9:
                r_loc = (2, 2)
        else:
            if n == 2:
                l_dist = find_distance(l_loc, (0, 1))
                r_dist = find_distance(r_loc, (0, 1))
                if l_dist > r_dist:
                    answer += "R"
                    r_loc = (0, 1)
                elif l_dist < r_dist:
                    answer += "L"
                    l_loc = (0, 1)
                elif l_dist == r_dist:
                    if hand == "left":
                        answer += "L"
                        l_loc = (0, 1)
                    elif hand == "right":
                        answer += "R"
                        r_loc = (0, 1)
            elif n == 5:
                l_dist = find_distance(l_loc, (1, 1))
                r_dist = find_distance(r_loc, (1, 1))
                if l_dist > r_dist:
                    answer += "R"
                    r_loc = (1, 1)
                elif l_dist < r_dist:
                    answer += "L"
                    l_loc = (1, 1)
                elif l_dist == r_dist:
                    if hand == "left":
                        answer += "L"
                        l_loc = (1, 1)
                    elif hand == "right":
                        answer += "R"
                        r_loc = (1, 1)
            elif n == 8:
                l_dist = find_distance(l_loc, (2, 1))
                r_dist = find_distance(r_loc, (2, 1))
                if l_dist > r_dist:
                    answer += "R"
                    r_loc = (2, 1)
                elif l_dist < r_dist:
                    answer += "L"
                    l_loc = (2, 1)
                elif l_dist == r_dist:
                    if hand == "left":
                        answer += "L"
                        l_loc = (2, 1)
                    elif hand == "right":
                        answer += "R"
                        r_loc = (2, 1)
            elif n == 0:
                l_dist = find_distance(l_loc, (3, 1))
                r_dist = find_distance(r_loc, (3, 1))
                if l_dist > r_dist:
                    answer += "R"
                    r_loc = (3, 1)
                elif l_dist < r_dist:
                    answer += "L"
                    l_loc = (3, 1)
                elif l_dist == r_dist:
                    if hand == "left":
                        answer += "L"
                        l_loc = (3, 1)
                    elif hand == "right":
                        answer += "R"
                        r_loc = (3, 1)
    return answer



# # -*- coding: utf-8 -*-
# """
# Created on Sat May 21 18:01:52 2022
#
# @author: Wonseok
# """
# def solution(numbers, hand):
#
#     answer = ''
#     current_L = '*'
#     current_R = '#'
#
#     def get_distance(cur, target):
#         if cur == target:
#             return 0
#
#         if target == 2:
#             if cur in [1, 3, 5]:
#                 return 1
#             elif cur in [4, 6, 8]:
#                 return 2
#             elif cur in [7, 9, 0]:
#                 return 3
#             else:
#                 return 4
#         elif target == 5:
#             if cur in [2, 4, 6, 8]:
#                 return 1
#             elif cur in [1, 3, 7, 9, 0]:
#                 return 2
#             else:
#                 return 3
#         elif target == 8:
#             if cur in [5, 7, 9, 0]:
#                 return 1
#             elif cur in [2, 4, 6, '*', '#']:
#                 return 2
#             else:
#                 return 3
#         else:
#             if cur in [8, '*', '#']:
#                 return 1
#             elif cur in [5, 7, 9]:
#                 return 2
#             elif cur in [2, 4, 6]:
#                 return 3
#             else:
#                 return 4
#
#     for i, n in enumerate(numbers):
#
#         if n in [1, 4, 7]:
#             current_L = n
#             answer += 'L'
#         elif n in [3, 6, 9]:
#             current_R = n
#             answer += 'R'
#         else:
#             distance_R = get_distance(current_R, n)
#             distance_L = get_distance(current_L, n)
#             if hand == 'right':
#                 if distance_R <= distance_L:
#                     current_R = n
#                     answer += 'R'
#                 else:
#                     current_L = n
#                     answer += 'L'
#             else:
#                 if distance_L <= distance_R:
#                     current_L = n
#                     answer += 'L'
#                 else:
#                     current_R = n
#                     answer += 'R'
#
#     return answer
#
# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
# print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
#
# # 다른 사람 풀이
# def solution(numbers, hand):
#     answer = ''
#     Lnumber = [1, 4, 7]
#     Rnumber = [3, 6, 9]
#     Lhand = [3, 0]
#     Rhand = [3, 2]
#     pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
#
#     for n in numbers:
#         for i in range(4):
#             for j in range(3):
#                 if pad[i][j] == n:
#                     if n in Lnumber:
#                         answer += 'L'
#                         Lhand = [i,j]
#                     elif n in Rnumber:
#                         answer += 'R'
#                         Rhand = [i,j]
#                     else:
#                         Lindex = abs(Lhand[0] - i) + abs(Lhand[1] - j)
#                         Rindex = abs(Rhand[0] - i) + abs(Rhand[1] - j)
#                         if Lindex < Rindex:
#                             answer += 'L'
#                             Lhand = [i, j]
#                         elif Lindex > Rindex:
#                             answer += 'R'
#                             Rhand = [i, j]
#                         elif Lindex == Rindex:
#                             if hand == "right":
#                                 answer += 'R'
#                                 Rhand = [i, j]
#                             else:
#                                 answer += 'L'
#                                 Lhand = [i, j]
#
#     return answer
#
# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
# print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))