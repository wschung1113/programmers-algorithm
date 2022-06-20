import heapq


def solution(scoville, K):
    answer = 0
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)

    while len(heap) > 1:
        least = heapq.heappop(heap)
        second = heapq.heappop(heap)
        mix = least + 2 * second
        heapq.heappush(heap, mix)
        answer += 1
        if all(h >= K for h in heap):
            return answer

    return -1