def solution(keymap, targets):
    answer = []
    min_dict = {}
    for t in targets:
        cnt = 0
        for c in t:
            if c in min_dict:
                cnt += min_dict[c]
            else:
                c_indexes = [k.index(c) + 1 for k in keymap if c in k]
                if c_indexes == []:
                    answer.append(-1)
                    break
                min_dict[c] = min(c_indexes)
                cnt += min_dict[c]
        else:
            answer.append(cnt)
    return answer

print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))