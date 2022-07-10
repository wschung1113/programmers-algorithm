# 나의 풀이
def solution(p):
    def split_u_v(s):
        l_counter = 0
        r_counter = 0
        for char in s:
            if char == "(":
                l_counter += 1
            else:
                r_counter += 1
            if l_counter == r_counter:
                break
        u = s[:2*l_counter]
        v = s[2*l_counter:]

        return u, v

    def is_proper(u):
        l_counter = 0
        r_counter = 0
        for char in u:
            if char == "(":
                l_counter += 1
            else:
                r_counter += 1
            if r_counter > l_counter:
                return False

        return True

    def flip(s):
        tmp = ""
        for char in s:
            if char == "(":
                tmp += ")"
            else:
                tmp += "("
        return tmp

    u, v = split_u_v(p)
    if is_proper(u):
        if len(v) == 0:
            return u
        else:
            return u + solution(v)
    else:
        tmp = "("
        tmp += solution(v) + ")"
        tmp += flip(u[1:-1])
        return tmp

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))










