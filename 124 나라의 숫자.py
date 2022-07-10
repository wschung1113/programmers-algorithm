n = 20

def solution(n):
    result = []
    while n: # n이 자연수일 때는 True, 계속 1씩 빼서 0이 되면 False
        t = n % 3 # n을 3으로 나눈 나머지
        if not t: # 나머지가 0이면 True
            t = 3 # 왜 나머지를 3으로 설정하고 n에서 1을 빼는지 이해가 안 감
            n -= 1
        result.append(str(t))
        print(result)
        n //= 3
    print(result[::-1])
    for i in range(len(result)):
        if result[i] == '3':
            result[i] = '4'
    return ''.join(result[::-1])

print(solution(20))
print(solution(6))

2 % 3