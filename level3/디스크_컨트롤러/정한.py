# 2레벨     코딩테스트 고득점 Kit     디스크 컨트롤러
import heapq as hq
from collections import deque


def solution(jobs):
    deq = deque(sorted(jobs))
    heap = []
    time = 0
    result = 0
    while deq or heap:
        while deq and deq[0][0] <= time:
            t = deq.popleft()
            hq.heappush(heap, (t[1], t[0]))

        if heap:
            t = hq.heappop(heap)
            time += t[0]
            result += time - t[1]
        else:
            time += 1
    return int(result / len(jobs))


if __name__ == "__main__":
    print(solution([[0, 3], [1, 9], [2, 6]]))
