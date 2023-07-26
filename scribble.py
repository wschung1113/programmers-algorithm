def solution(arr1, arr2):
    # ans = []
    # n = len(arr2[0])
    # for i, row in enumerate(arr1):
    #     tmp = []
    #     for k in range(n):
    #         sm = 0
    #         for j, a in enumerate(row):
    #             sm += a * arr2[j][k]
    #         tmp.append(sm)
    #     ans.append(tmp)
    # return ans

    return [[sum([a * b for a, b in [zip(arr1_row, arr2_col) for arr2_col in zip(*arr2)]]) for arr2_col] for arr1_row in arr1]

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]

# print([[sum(a * b for a, b in list(zip(arr1_row, arr2_col))) for arr2_col in arr2] for arr1_row in arr1])
print([[sum(a * b for a, b in list(zip(arr1_row, arr2_col))) for arr2_col in zip(*arr2)] for arr1_row in arr1])

for a in arr1):
    for b in arr2:
        print(a, b)
        print(list(zip(a, b)))

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))