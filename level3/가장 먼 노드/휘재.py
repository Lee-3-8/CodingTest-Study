from collections import deque, defaultdict

def make_graph(edge):
    graph = defaultdict(lambda: {'conn':[], 'dist':float('inf')})
    for s, t in edge:
        graph[s]['conn'].append(t)
        graph[t]['conn'].append(s)
    return graph

def solution(n, edge):
    graph, q = make_graph(edge), deque([(1, 0)])
    dist_dic, max_dist = defaultdict(int), 0
    while q:
        node, dist = q.popleft()
        if graph[node]['dist'] > dist:
            graph[node]['dist'] = dist
            max_dist = max(max_dist, dist)
            dist_dic[max_dist] += 1
            for tgt in graph[node]['conn']:
                if graph[tgt]['dist'] > dist + 1:
                    q.append((tgt, dist + 1))

    return dist_dic[max_dist]

if __name__ == '__main__':
    print((solution(
        6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])))