# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 20:32:41 2022

@author: Wonseok
"""

import collections
import itertools
import numpy as np

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        unique_combinations = list(set(order_combinations))
        most_ordered = sorted([(u, order_combinations.count(u)) for u in unique_combinations], key=lambda x: x[1], reverse=True)
        # most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))