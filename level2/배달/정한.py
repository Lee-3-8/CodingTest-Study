from collections import defaultdict, deque
import heapq as hq


def solution(N, road, K):
    dic = defaultdict(set)
    gp = [float("inf")] * (N + 1)
    for s, e, w in road:
        dic[s].add((e, w))
        dic[e].add((s, w))

    que = []
    hq.heappush(que, (0, 1))
    gp[1] = 0
    while que:
        cur_dis, node = hq.heappop(que)
        for e, w in dic[node]:
            if gp[e] > cur_dis + w:
                gp[e] = cur_dis + w
                hq.heappush(que, (gp[e], e))

    cnt = 0
    for i in gp:
        if i <= K:
            cnt += 1
    return cnt


if __name__ == "__main__":
    print(
        solution(
            6,
            [
                [1, 2, 1],
                [1, 3, 2],
                [2, 3, 2],
                [3, 4, 3],
                [3, 5, 2],
                [3, 5, 3],
                [5, 6, 1],
            ],
            4,
        )
    )
