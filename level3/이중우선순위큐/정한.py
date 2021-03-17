# 3레벨     코딩테스트 고득점 Kit     이중우선순위큐
from collections import defaultdict
import heapq as hq


def solution(operations):
    max_h = []
    min_h = []
    dic = defaultdict(int)
    for i in operations:
        com, num = i.split(" ")
        if com == "I":
            hq.heappush(min_h, int(num))
            hq.heappush(max_h, -int(num))
            dic[int(num)] += 1

        else:
            while num == "-1" and min_h:
                n = hq.heappop(min_h)
                if dic[n] != 0:
                    dic[n] -= 1
                    break

            while num == "1" and max_h:
                n = hq.heappop(max_h)
                if dic[-n] != 0:
                    dic[-n] -= 1
                    break
    max = min = 0
    while min_h:
        n = hq.heappop(min_h)
        if dic[n] != 0:
            dic[n] -= 1
            min = n
            break

    while max_h:
        n = hq.heappop(max_h)
        if dic[-n] != 0:
            dic[-n] -= 1
            max = -n
            break

    return [max, min]


if __name__ == "__main__":
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
