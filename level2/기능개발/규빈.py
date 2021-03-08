from math import ceil
from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    cnt = 1

    while progresses:
        p = progresses.popleft()
        s = speeds.popleft()
        if p >= 100:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            n = ceil((100-p)/s)
            for i in range(len(speeds)):
                progresses[i] += speeds[i]*n
    answer.append(cnt)

    return answer[1:]