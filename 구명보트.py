# 나의 풀이 1
# 효율성 미충족
# people = [70, 50, 80, 50]
# limit = 100
# def solution(people, limit):
#     answer = 0
#     people = sorted(people)
#     while len(people) != 0:
#         boat_available = limit
#         possible_people = [p for p in people if p <= boat_available]
#         n_people_onb = 0
#         while len(possible_people) != 0 and n_people_onb < 2:
#             person = possible_people.pop(-1)
#             people.remove(person)
#             n_people_onb += 1
#             boat_available -= person
#             possible_people = [p for p in people if p <= boat_available]
#         answer += 1
#
#     return answer


# 나의 풀이 2
from collections import deque

people = [70, 50, 80, 50]
limit = 100
def solution(people, limit):
    answer = 0
    deque_people = deque(sorted(people))
    while len(deque_people) != 0:
        answer += 1
        heaviest = deque_people.pop()
        if not deque_people:
            break
        if heaviest + deque_people[0] <= limit:
            deque_people.popleft()


    return answer


# 다른 사람의 풀이 1
# from collections import deque
#
# people = [70, 50, 80, 50]
# limit = 100
# def solution(people, limit):
#     result = 0
#     deque_people = deque(sorted(people))
#
#     while deque_people:
#         left = deque_people.popleft()
#         if not deque_people:
#             return result + 1
#         right = deque_people.pop()
#         if left + right > limit:
#             deque_people.appendleft(left)
#         result += 1
#     return result

print(solution([70, 50, 80, 50], 100))