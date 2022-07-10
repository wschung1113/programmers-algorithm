# 다른 사람의 풀이 1
rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
# a, b, c, d = 2, 2, 5, 4
# def solution(rows, columns, queries):
#     answer = []
#
#     board = [[i+(j)*columns for i in range(1,columns+1)] for j in range(rows)]
#     # print(board)
#     # [[1, 2, 3, 4, 5, 6],
#     #  [7, 8, 9, 10, 11, 12],
#     #  [13, 14, 15, 16, 17, 18],
#     #  [19, 20, 21, 22, 23, 24],
#     #  [25, 26, 27, 28, 29, 30],
#     #  [31, 32, 33, 34, 35, 36]]
#     for a,b,c,d in queries:
#         stack = []
#         r1, c1, r2, c2 = a-1, b-1, c-1, d-1
#
#         for i in range(c1, c2+1):
#             stack.append(board[r1][i])
#             if len(stack) == 1:
#                 continue
#             else:
#                 board[r1][i] = stack[-2]
#
#
#         for j in range(r1+1, r2+1):
#             stack.append(board[j][i])
#             board[j][i] = stack[-2]
#
#         for k in range(c2-1, c1-1, -1):
#             stack.append(board[j][k])
#             board[j][k] = stack[-2]
#
#         for l in range(r2-1, r1-1, -1):
#             stack.append(board[l][k])
#             board[l][k] = stack[-2]
#
#         answer.append(min(stack))
#
#
#     return answer


# 내가 위 코드 안 보고 그대로 짜보기
def solution(rows, columns, queries):
    answer = []

    # create board
    board = [[i+j*columns for i in range(1, rows+1)] for j in range(rows)]
    # print(board)
    # [[1, 2, 3, 4, 5, 6],
    #  [7, 8, 9, 10, 11, 12],
    #  [13, 14, 15, 16, 17, 18],
    #  [19, 20, 21, 22, 23, 24],
    #  [25, 26, 27, 28, 29, 30],
    #  [31, 32, 33, 34, 35, 36]]
    # apply queries
    for a, b, c, d in queries:
        stack = []
        r1, c1, r2, c2 = a-1, b-1, c-1, d-1

        for i in range(c1, c2+1):
            stack.append(board[r1][i])
            if len(stack) < 2:
                continue
            else:
                board[r1][i] = stack[-2]

        for j in range(r1+1, r2+1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]

        for k in range(c2-1, c1-1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]

        for m in range(r2-1, r1-1, -1):
            stack.append(board[m][k])
            board[m][k] = stack[-2]

        answer.append(min(stack))


    return answer


# 다른 사람의 풀이 2
# from collections import deque
#
# def solution(rows, columns, queries):
#     arr = [[i+columns*j for i in range(1,columns+1)] for j in range(rows)]
#     answer, result = deque(), []
#     # i = queries[0]
#     for i in queries:
#         a,b,c,d = i[0]-1,i[1]-1,i[2]-1,i[3]-1
#         for x in range(d-b):
#             answer.append(arr[a][b+x])
#         for y in range(c-a):
#             answer.append(arr[a+y][d])
#         for z in range(d-b):
#             answer.append(arr[c][d-z])
#         for k in range(c-a):
#             answer.append(arr[c-k][b])
#         answer.rotate(1)
#         result.append(min(answer))
#         for x in range(d-b):
#             arr[a][b+x] = answer[0]
#             answer.popleft()
#         for y in range(c-a):
#             arr[a+y][d] = answer[0]
#             answer.popleft()
#         for z in range(d-b):
#             arr[c][d-z] = answer[0]
#             answer.popleft()
#         for k in range(c-a):
#             arr[c-k][b] = answer[0]
#             answer.popleft()
#
#     return result

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))





















