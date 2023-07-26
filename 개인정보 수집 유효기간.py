def solution(today, terms, privacies):
    answer = []
    today_days = int(today.split(".")[0]) * (12 * 28) + (int(today.split(".")[1])-1) * 28 + int(today.split(".")[2])
    terms_days = dict(zip([t[0] for t in terms], [int(t.split(" ")[-1]) * 28 for t in terms]))
    for ix, p in enumerate(privacies, start=1):
        term = p[-1]
        p_days = int(p[:-2].split(".")[0]) * (12 * 28) + (int(p[:-2].split(".")[1]) - 1) * 28 + int(p[:-2].split(".")[2])
        # print(today_days, p_days)
        # print(today_days - p_days, terms_days[term])
        if today_days - p_days >= terms_days[term]:
            answer.append(ix)

    return answer

# print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))