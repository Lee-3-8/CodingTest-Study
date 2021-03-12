from heapq import heapify, heappop, heappush
def solution(jobs):
    answer = 0
    cur, cnt = 0, len(jobs)
    heap = []
    heapify(jobs)
    while jobs or heap:
        while jobs:
            if jobs[0][0] > cur:
                break
            enter, processing = heappop(jobs)
            heappush(heap, (processing, enter))

        if not heap: # 남은 작업이 현재 시간 후에 들어오는 작업들만 남음
            enter, processing = jobs[0]
            cur = enter
            continue

        p, e = heappop(heap)
        answer += cur - e + p
        cur += p
        
    return answer//cnt