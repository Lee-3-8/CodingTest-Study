# 2레벨     코딩테스트 고득점 Kit     기능개발
from math import ceil
from collections import deque


def solution(progresses, speeds):
    work = deque([(100 - p) / s for p, s in zip(progresses, speeds)])
    result = []
    while work:
        complete = ceil(work.popleft())
        cnt = 1
        while work and complete >= work[0]:
            cnt += 1
            work.popleft()
        result.append(cnt)
    return result


if __name__ == "__main__":
    print(solution([93, 30, 55], [1, 30, 5]))
