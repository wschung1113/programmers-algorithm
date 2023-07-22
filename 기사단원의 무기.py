def get_divisor_count(n):
    cnt = 0
    for i in range(1, int(pow(n, .5)) + 1):
        if n % i == 0:
            if n // i == i:
                cnt += 1
            else:
                cnt += 2
    return cnt

def solution(number, limit, power):
    answer = 0
    for n in range(1, number + 1):
        n_divisor = get_divisor_count(n)
        if n_divisor > limit:
            answer += power
        else:
            answer += n_divisor
    return answer