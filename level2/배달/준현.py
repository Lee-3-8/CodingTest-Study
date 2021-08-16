from heapq import heappush, heappop
from collections import defaultdict


def solution(N, road, K):
    graph = defaultdict(lambda: {})
    answer = 0
    for a, b, c in road:
        print(a, b, c)
        graph[a][b] = c
        graph[b][a] = c
    for a, b, c in road:
        if graph[a][b] > c:
            graph[a][b] = c
        if graph[b][a] > c:
            graph[b][a] = c
    print(graph)
    start = 1
    distances = {node: float('inf') for node in range(1, N+1)}
    distances[start] = 0
    queue = []
    heappush(queue, [distances[start], start])
    while queue:
        current_distance, current_destination = heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heappush(queue, [distance, new_destination])
    for i in distances.values():
        if i <= K:
            answer += 1
    return answer


N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
k = 3
print(solution(N, road, k))
