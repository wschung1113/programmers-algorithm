def solution(n, m, section):
    if m == 1:
        return len(section)
    elif m == n:
        return 1

    answer = 0
    while section:
        answer += 1
        s = section[0]
        stroke = s + m - 1
        section.pop(0)
        while section:
            if section[0] <= stroke:
                section.pop(0)
                if section == []:
                    break
            else:
                break

    return answer