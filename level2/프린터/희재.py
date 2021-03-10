from collections import deque
from heapq import heappop, heapify

def solution(priors, location):
    q = deque(enumerate(priors))
    heap = list(map(lambda x: -x, priors))
    heapify(heap)
    
    answer = 0
    while priors:
        idx, prior = q.popleft()

        if -heap[0] == prior:
            answer += 1
            heappop(heap)
            if idx == location:
                return answer
        else:
            q.append((idx, prior))


if __name__ == '__main__':
    print(solution( [1, 1, 9, 1, 1, 1], 0))