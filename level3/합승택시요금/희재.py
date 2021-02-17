from heapq import heappush, heappop
from collections import defaultdict

def get_graph(fares):
    graph = defaultdict(lambda: {})
    for src, tgt, dist in fares:
        graph[src].update({tgt:dist})
        graph[tgt].update({src:dist})
    return graph

def get_dist(n, graph, src, tgts):
    dists = {v: float('inf') for v in range(1, n+1)}
    dists[src], heap = 0, []
    heappush(heap, [dists[src], src])

    while heap:
        cur_dist, cur_tgt = heappop(heap)
        if dists[cur_tgt] >= cur_dist:
            for next_tgt, next_dist in graph[cur_tgt].items():
                if cur_dist + next_dist < dists[next_tgt]:
                    dists[next_tgt] = cur_dist + next_dist
                    heappush(heap, [dists[next_tgt], next_tgt])

    return sum([dists[tgt] for tgt in tgts])

def solution(n, s, a, b, fares, answer=float('inf')):
    graph = get_graph(fares)
    for i in range(1, n+1):
        answer = min(
            answer,
            get_dist(n, graph, s, [i]) + get_dist(n, graph, i, [a, b])
        )
    return answer
