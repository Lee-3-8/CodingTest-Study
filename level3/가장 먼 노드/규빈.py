from collections import deque

def bfs(graph, root):
    visited = [False] * (len(graph) + 1)
    dis = [0] * (len(graph) + 1)
    queue = deque([root])
    cnt = 0

    while queue:
        for i in range(len(queue)):
            n = queue.popleft()
            if not visited[n]:
                visited[n] = True
                dis[n] = cnt
                queue += graph[n] - set(visited)
        cnt += 1
    return dis

def solution(n, edge):
    graph = {i+1:set() for i in range(n)}
    for l in edge:
        graph[l[0]].add(l[1])
        graph[l[1]].add(l[0])
    dis = bfs(graph,1)

    return dis.count(max(dis))