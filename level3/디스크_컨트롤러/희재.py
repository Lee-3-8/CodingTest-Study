from heapq import heappush, heappop
from collections import deque

def solution(jobs, answer=0):
    jobs_len = len(jobs)
    jobs = deque(sorted(jobs))
    cur, heap = jobs[0][0], []

    while jobs or heap:
        if not heap and cur < jobs[0][0]:
            cur = jobs[0][0]
        while jobs and jobs[0][0] <= cur:
            start, time = jobs.popleft()
            heappush(heap, (time, start))
        if heap:
            time, start = heappop(heap)
            answer += (cur - start) + time
            cur += time

    return answer // jobs_len