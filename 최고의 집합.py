def solution(n, s):
    if n > s:
        return [-1]
    di, mo = divmod(s, n)
    if mo == 0:
        answer = [di] * n
    else:
        answer = [di] * (n - mo) + [di + 1] * (mo)
    return answer