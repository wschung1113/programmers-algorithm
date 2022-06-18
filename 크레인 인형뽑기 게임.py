# -*- coding: utf-8 -*-
"""
Created on Sun May 22 23:04:32 2022

@author: Wonseok
"""

# 나의 풀이
def solution(board, moves):
    answer = 0
    basket = []
    
    for i, m in enumerate(moves):
        cur_board = board[m-1]
        for j in range(1, len(cur_board)+1):
            if cur_board[-j] == 0:
                continue
            else:
                basket.append(cur_board[-j])
                cur_board[-j] = 0
                break
                
    done = False
    while not done:
        prev_n = basket[0]
        L = len(basket)
        for k in range(1, L):
            cur_n = basket[k]
            if prev_n == cur_n:
                basket.pop(k-1)
                basket.pop(k-1)
                answer += 2
                break
            else:
                prev_n = cur_n
        if L == len(basket):
            done = True
        
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
        
# 다른 사람 풀이

def solution(board,moves):
    answer =0 
    box =[]

    for move in moves:
        # print(move)
        for doll in board:
            # print(doll)
            # print(doll[move-1])
            # print(doll[move-1] != 0)
            if(doll[move-1] != 0):
                box.append(doll[move-1])
                doll[move-1] =0
                break
        print(box)
        if(len(box) >= 2):
            if(box[len(box) -1] == box[len(box) -2]):
                box.pop()
                box.pop()
                answer +=2
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))







        