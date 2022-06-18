# 내 풀이
def solution(id_list, report, k):
    if k > max(len(id_list), len(report)):
        return [0] * len(id_list)
    
    answer = [0] * len(id_list)
    dup_case = []
    reported_cnt = [0] * len(id_list)
    banned = []
    
    for i, s in enumerate(report):
        if s in dup_case:
            continue
        dup_case.append(s)
        reporter = s.split(' ')[0]
        reportee = s.split(' ')[1]
        reported_cnt[id_list.index(reportee)] += 1
        if reported_cnt[id_list.index(reportee)] >= k and reportee not in banned:
            # print(reportee)
            banned.append(reportee)
    # print(reported_cnt)
    
    for s in dup_case:
        # print(s)
        if s.split(' ')[1] in banned:
            answer[id_list.index(s.split(' ')[0])] += 1
    
    # print(banned)
    # print(dup_case)
    
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))



# 다른 사람 풀이
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
def solution(id_list, report, k):
    s1 = [s.split()[1] for s in set(report)] # reportees
    s2 = [s for s in set(s1) if s1.count(s) >= k]
    s3 = [s.split()[0] for s in set(report) if s.split()[1] in s2]
    return [s3.count(i) for i in id_list]

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))









































