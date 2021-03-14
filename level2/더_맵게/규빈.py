import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    for _ in range(len(heap)):
        a = heapq.heappop(heap)
        if a >= K:
            return answer
        if not heap:
            return -1
        b = heapq.heappop(heap)
        c = a + b * 2
        heapq.heappush(heap, c)
        answer += 1