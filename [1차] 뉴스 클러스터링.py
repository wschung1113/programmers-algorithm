from math import floor

str1 = "handshake"
str2 = "shake hands"
def solution(str1, str2):
    # answer = 0
    str1, str2 = str1.lower(), str2.lower()
    multiset_1 = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    multiset_2 = [str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    # print(multiset_1)
    # print(multiset_2)

    def get_numerator_set(set1, set2):
        ans = []
        unique_set1 = list(set(set1))
        for stri in unique_set1:
            if stri in set2:
                for i in range(min(set1.count(stri), set2.count(stri))):
                    ans.append(stri)
        return ans

    def get_denominator_set(set1, set2):
        ans = []
        unique_set = list(set(set1 + set2))
        for stri in unique_set:
            for i in range(max(set1.count(stri), set2.count(stri))):
                ans.append(stri)
        return ans

    numerator_list = get_numerator_set(multiset_1, multiset_2)
    # print(numerator_list)
    numerator = len(numerator_list)

    denominator_list = get_denominator_set(multiset_1, multiset_2)
    # print(denominator_list)
    denominator = len(denominator_list)

    if numerator == 0 and denominator == 0:
        return 1 * 65536

    answer = floor(numerator / denominator * 65536)

    return answer

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))