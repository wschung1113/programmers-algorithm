def solution(lottos, win_nums):
    num_same = sum([True for l in lottos if l in win_nums])

    def get_rank(num):
        if num == 6:
            return 1
        elif num == 5:
            return 2
        elif num == 4:
            return 3
        elif num == 3:
            return 4
        elif num == 2:
            return 5
        else:
            return 6

    answer = [get_rank(num_same + lottos.count(0)), get_rank(num_same)]

    return answer