import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while len(scoville) > 1:
        print(scoville)
        if scoville[0] < K:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first + 2 * second)
            cnt += 1

        else: break

    return cnt if scoville[0] > K else -1

print(solution([1,1], 7))