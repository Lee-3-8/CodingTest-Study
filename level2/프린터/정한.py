# 2레벨     코딩테스트 고득점 Kit       프린터
from collections import deque


def solution(priorities, location):
    order = deque(sorted(priorities, reverse=True))
    priorities = deque([(p, _id) for _id, p in enumerate(priorities)])
    cnt = 0
    while priorities:
        t = priorities.popleft()
        if t[0] == order[0]:
            cnt += 1
            order.popleft()
            if t[1] == location:
                return cnt
        else:
            priorities.append(t)


if __name__ == "__main__":
    print(solution([1, 1, 9, 1, 1, 1], 0))