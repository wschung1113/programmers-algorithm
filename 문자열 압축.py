# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 23:00:48 2022

@author: Wonseok
"""

# 내 예전 답변
def solution(s):
    def compress(s, size): # returns the compressed string
        comp = ""
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        pattern_word = s[0:size]
        count = 1
        for i in range(size, len(s), size):
            word = s[i:i + size]
            if word == pattern_word:
                count += 1
            else:
                if count > 1:
                    comp = comp + str(count) + pattern_word    
                    pattern_word = word
                    count = 1
                else:
                    comp = comp + pattern_word
                    pattern_word = word
                    count = 1
            if i + size >= len(s):
                if count > 1:
                    comp = comp + str(count) + pattern_word    
                    pattern_word = word
                    count = 1
                else:
                    comp = comp + pattern_word
                    pattern_word = word
                    count = 1
        return comp
    
    answer = 0
    cand = []  # candidate
    for comp_size in range(1, len(s)):
        cand.append(len(compress(s, comp_size)))
    return min(cand)

# 나의 최근 답변
# def solution(s):
#     if len(s) == 1:
#         return 
#     def compress(s, size):
#         # s = 'aabbaccc'
#         # size = 1
#         out = ''
#         count = 1
#         left_idx = 0
#         right_idx = left_idx + size
#         while right_idx <= len(s):
#             pattern = s[left_idx:right_idx]
#             # print(pattern)
#             for j in range(right_idx, len(s), size):
#                 if s[j:j+size] == pattern:
#                     count += 1
#                 else:
#                     if count == 1:
#                         out += pattern
#                     else:
#                         out += str(count) + pattern
#                     left_idx = j
#                     right_idx = left_idx + size
#                     count = 1
#                     break
#             if j == len(s) - size:
#                 if count == 1:
#                     out += pattern
#                 else:
#                     out += str(count) + pattern
#                 break      
#         print(out)
#         return out
    
#     cand = [len(s)]  # 안 줄이는게 젤 나을수도 있음
#     for comp_size in range(1, len(s)//2+1):
#         cand.append(len(compress(s, comp_size)))
#     return min(cand)

def solution(s):
    s = 'aabbaccc'
    answer = len(s)
    def compress(s, pat_len):
        tokens = [s[i:i+pat_len] for i in range(0, len(s), pat_len)]
        next_words = tokens[1:] + ['']
        cnt = 1
        res = []
        cur_word = tokens[0]
        for a, b in zip(tokens, next_words):
            if a == b:
                cnt += 1
            else:
                res.append([cur_word, cur_cnt])
                cur_word = b
                cur_cnt = 1
        return res

return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)    


for word, cnt in res:
    print(word)
    print(cnt)
    if cnt > 1:

        print(len(word))

        print(len(str(cnt)))

    else:
        print('meh')
    
    for pat_len in range(1, len(s)//2+1):
        # tokens = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
        
        
    return answer

print(solution('aabbaccc'))
print(solution("ababcdcdababcdcd"))




# 다른 사람의 풀이 1
text = 'aabbaccc'
tok_len = 1
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):        
        if a == b:
            cur_cnt += 1
        else:
            # print(cur_word)
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)



def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))












































































