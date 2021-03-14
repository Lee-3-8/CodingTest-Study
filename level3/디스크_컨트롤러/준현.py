from collections import deque
from heapq import heappush, heappop


def solution(jobs):
    jobs = deque(sorted(jobs))
    jobs_len = len(jobs)
    pri_arr = []
    cur_time = 0
    finish_job = 0
    answer = 0
    while finish_job < jobs_len:
        if not pri_arr:
            start, time = jobs.popleft()
            cur_time = start+time
            answer += time
        else:
            time, start = heappop(pri_arr)
            cur_time += time
            answer += cur_time-start
        finish_job += 1
        while jobs and jobs[0][0] <= cur_time:
            heappush(pri_arr, jobs.popleft()[::-1])

    return answer//jobs_len


jobs = [[0, 3], [4, 4], [5, 3], [4, 1]]
print(solution(jobs))
