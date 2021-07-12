from collections import defaultdict
import sys
sys.setrecursionlimit(300000)


def dfs(x, a, dic, visited):
    global answer
    visited.add(x)

    for i in dic[x]:
        if i not in visited:
            a[x] += dfs(i, a, dic, visited)
    answer += abs(a[x])
    return a[x]


def solution(a, edges):
    global answer
    answer = 0
    dic = defaultdict(list)

    if sum(a) != 0:
        return -1
    for i in range(len(edges)):
        dic[edges[i][0]].append(edges[i][1])
        dic[edges[i][1]].append(edges[i][0])
    visited = set()
    visited.add(0)
    dfs(0, a, dic, visited)

    return answer


a = [-5, 0, 2, 1, 2]
edges = [[0, 1], [3, 4], [2, 3], [0, 3]]
print(solution(a, edges))
