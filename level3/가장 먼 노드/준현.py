from collections import defaultdict, deque


def bfs(graph, answer, n):
    queue = deque()
    queue.append((1, 0))
    visited = [True]*(n+1)
    visited[1] = False
    while queue:
        start, dis = queue.popleft()
        for i in graph[start]:
            if visited[i]:
                visited[i] = False
                answer[i] = dis+1
                print(answer[i], i)
                queue.append((i, dis+1))


def init(graph, edge):
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])


def solution(n, edge):
    graph = defaultdict(lambda: [])
    init(graph, edge)
    answer = defaultdict(int)
    answer[1] = 0
    bfs(graph, answer, n)
    print(answer)
    max_dis = 0
    dis = []
    for i in range(1, n+1):
        if max_dis < answer[i]:
            max_dis = answer[i]
            dis = [i]
        elif max_dis == answer[i]:
            dis.append(i)
    return len(dis)


n = 5
vertex = [[1, 2], [2, 3], [2, 4], [4, 5], [1, 5]]
print(solution(n, vertex))
