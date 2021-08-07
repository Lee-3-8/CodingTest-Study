from collections import defaultdict
def solution(N, road, K):
    answer = 0
    graph = [[0] * N for _ in range(N)]
    distance = [float("inf")] * N

    for n1, n2, w in road:
        if not graph[n1-1][n2-1] or graph[n1-1][n2-1] > w:
            graph[n1-1][n2-1] = w
            graph[n2-1][n1-1] = w

    queue = [0]

    while queue:
        n = queue.pop()
        for i in range(N):
            if graph[n][i] and distance[i] >= distance[n] + graph[n][i]:
                if distance[n] == float("inf"):
                    distance[i] = graph[n][i]
                else:
                    distance[i] = distance[n] + graph[n][i]
                queue.append(i)

    for i in range(1,N):
        if distance[i] <= K:
            answer += 1

    return answer+1