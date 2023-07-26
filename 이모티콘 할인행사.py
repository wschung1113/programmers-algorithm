from itertools import permutations, product


def solution(users, emoticons):
    n_emot = len(emoticons)
    # ls = [10, 20, 30, 40] * n_emot
    # res = permutations(ls, n_emot)
    res = list(product([10, 20, 30, 40], repeat=n_emot))

    prev_cnt = 0
    prev_sales = 0

    for r in res:
        cnt = 0
        sales = 0
        for u in users:
            usr_sale = 0
            thr_disc = u[0]
            thr_price = u[1]
            for ix, d in enumerate(r):
                if d >= thr_disc:
                    usr_sale += emoticons[ix] * (100 - d) / 100
            if usr_sale >= thr_price:
                cnt += 1
            else:
                sales += usr_sale
        if cnt > prev_cnt:
            prev_cnt = cnt
            prev_sales = sales
        elif cnt == prev_cnt and sales > prev_sales:
            prev_sales = sales

    return [prev_cnt, prev_sales]

print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))