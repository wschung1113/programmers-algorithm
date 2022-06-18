# -*- coding: utf-8 -*-
"""
Created on Sat May 21 16:08:13 2022

@author: Wonseok
"""
# 내 풀이
new_id = '=.='
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    
    for c in new_id:
        if c.isalnum() or c in ['-', '_', '.']:
            answer += c
    
    # new_answer = answer
    # for i, c in enumerate(answer):
    #     if i == 0:
    #         prev_char = c
    #     if c == '.' and prev_char == '.':
    #         new_answer = answer[:i] + answer[i+1:]
    #     else:
    #         prev_char = c
    
    # answer = new_answer
    
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
        
    if len(answer) == 0:
        answer = 'a'
        
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    if len(answer) <= 2:
        answer += answer[-1] * (3 - len(answer))
    
        
        
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))


# 다른 사람 풀이
def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    answer = ''
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4단계
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    # 5단계
    answer = 'a' if answer == '' else answer
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7단계
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3-len(answer))
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))