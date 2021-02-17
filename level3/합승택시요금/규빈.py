import heapq
def solution(n, s, a, b, fares):
    graph = {}
    minFare = float('inf')
    for i in range(n):
        graph[i+1] = {}
    
    for node1, node2, weight in fares:
        graph[node1][node2] = weight
        graph[node2][node1] = weight

    for i in range(1,n+1):
        middle_distance = dijkstra(graph,s,i)
        if middle_distance == float('inf'):
            continue
        middleA_distance = dijkstra(graph,i,a)
        middleB_distance = dijkstra(graph,i,b)
        curFare = middle_distance + middleA_distance + middleB_distance
        minFare = min(minFare, curFare)
    
    return minFare

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [start, distances[start]])

    while queue:
        current_destination, current_distance = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue
    
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [new_destination, distance])
    
    return distances[end]