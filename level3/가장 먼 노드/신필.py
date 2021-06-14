from collections import defaultdict, deque

def solution(n, edge):
    node = defaultdict(list)
    dist = [-1]*n
    for s, e in edge:
        node[s].append(e)
        node[e].append(s)

    que = deque([1])
    dist[0] = 0
    while que:
        cur_dist = dist[que[0]-1]
        for i in node[que.popleft()]:
            if dist[i-1] == -1:
                que.append(i)
                dist[i-1] = cur_dist + 1
    m = max(dist)
    return len(list(filter(lambda x: x == m, dist)))

if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
