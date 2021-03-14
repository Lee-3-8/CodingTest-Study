
import heapq
scoville = [1, 2, 3, 9, 10, 12]
k = 7


def solution(scoville, k):
    answer = 0
    if len(scoville) == 0:
        return -1
    heapq.heapify(scoville)
    while scoville[0] < k:
        answer += 1
        a = heapq.heappop(scoville)
        if not scoville:
            answer = -1
            break
        else:
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a+b*2)
    return answer


print(solution(scoville, k))
