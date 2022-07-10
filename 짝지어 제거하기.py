# 내 풀이
# def solution(s):
#     while len(s) > 0:
#         print(s)
#         couple_idx = [idx for idx, _ in enumerate(s[:-1]) if s[idx] == s[idx + 1]]
#         couple_idx = [idx for i, idx in enumerate(couple_idx[:-1]) if couple_idx[i+1] - couple_idx[i] > 1]
#
#         if len(couple_idx) == 0:
#             break
#         offset = 0
#         for idx in couple_idx:
#             s = s[:idx-offset] + s[idx+2-offset:]
#             offset += 2
#     if len(s) != 0:
#         return 0
#
#     return 1
#
# print(solution("baaabaa"))
# print(solution("cdcd"))


# 다른 사람 풀이
def solution(s):
    answer = []
    for char in s:
        if not answer:
            answer.append(char)
        else:
            if answer[-1] == char:
                answer.pop()
            else:
                answer.append(char)
    if len(answer) == 0:
        return 1
    else:
        return 0

    
print(solution("baaabaa"))
print(solution("cdcd"))