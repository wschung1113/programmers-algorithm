def solution(w, h):
    if w > h: # 큰 놈이 오른쪽
        w, h = h, w
    def gcd(a, b):
        return b if a == 0 else gcd(b % a, a)


    g = gcd(w, h)


    return (w * h - (g * (w // g + h // g - 1)))

print(solution(8, 12))
