# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 17:00:07 2022

@author: Wonseok
"""

# 나의 풀이
def solution(record):
    answer = []
    uid_nickname_dict = {}
    uid_record_dict = {}
    for r in record:
        if r.split(' ')[0] == 'Enter':
            uid_nickname_dict[r.split(' ')[1]] = r.split(' ')[2]
            if r.split(' ')[1] not in uid_record_dict.keys():
                uid_record_dict[r.split(' ')[1]] = [len(answer)]
            else:
                for i in uid_record_dict[r.split(' ')[1]]:
                    answer[i] = r.split(' ')[2] + '님이 ' + answer[i].split(' ')[1]
                uid_record_dict[r.split(' ')[1]] += [len(answer)]
            answer.append(uid_nickname_dict[r.split(' ')[1]] + '님이 들어왔습니다.')
        elif r.split(' ')[0] == 'Change':
            uid_nickname_dict[r.split(' ')[1]] = r.split(' ')[2]
            for i in uid_record_dict[r.split(' ')[1]]:
                answer[i] = r.split(' ')[2] + '님이 ' + answer[i].split(' ')[1]
        else:
            uid_record_dict[r.split(' ')[1]] += [len(answer)]
            answer.append(uid_nickname_dict[r.split(' ')[1]] + '님이 나갔습니다.')
                
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))


# 다른 사람의 풀이
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))














