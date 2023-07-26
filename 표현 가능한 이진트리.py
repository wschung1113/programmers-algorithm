from math import log2


def solution(numbers):
    ans = []
    for n in numbers:
        bin_n = bin(n)[2:]
        n_nodes = len(bin_n)
        n_total_nodes = (2 ** (int(log2(n_nodes)) + 1)) - 1
        tree_n = "0" * (n_total_nodes - n_nodes) + bin_n

        print(tree_n)

        center = n_total_nodes // 2
        if tree_n[center] == "0":
            ans.append(0)
            continue

        is_possible = 1
        stack = [[0, n_total_nodes - 1]]
        while stack:
            left, right = stack.pop()
            if left == right:
                continue

            center = (left + right + 1) // 2
            if tree_n[center] == "0" and "1" in tree_n[left: right + 1]:
                is_possible = 0
                break

            stack.extend([[left, center - 1], [center + 1, right]])
        ans.append(is_possible)

    return ans

print(solution([7, 42, 5]))