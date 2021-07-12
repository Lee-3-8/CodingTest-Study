from collections import deque, defaultdict

def solution(a, edges):
    answer = 0
    queue = deque([])
    
    graph = defaultdict(set)  
    for v1, v2 in edges:
        graph[v1].add(v2)
        graph[v2].add(v1)

    for name in graph:
        if len(graph[name]) == 1 and a[name]:
            queue.append(name)
    
    while queue:
        v1 = queue.popleft()
        if graph[v1]:
            v2 = list(graph[v1])[0]
            graph[v1].remove(v2)
        else:
            continue
        val = a[v1]
        graph[v2].remove(v1)
        if len(graph[v2]) == 1 and a[v2]:
            queue.append(v2)
        a[v1] -= val
        a[v2] += val
        answer += abs(val)

    return answer if not sum(a) else -1