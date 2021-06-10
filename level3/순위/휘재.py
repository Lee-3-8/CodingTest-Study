def make_graph(n, results):
    graph = {i:{'win':[], 'lose':[]} for i in range(1, n + 1)}
    for win, lose in results:
        graph[win]['win'].append(lose)
        graph[lose]['lose'].append(win)
    return graph

def solution(n, results):
    answer = 0
    graph = make_graph(n, results)

    def dfs(graph, start, route):
        visited.add(start)
        for tgt in graph[start][route]:
            if tgt not in visited:
                dfs(graph, tgt, route)

    for i in range(1, n + 1):
        visited = set()
        dfs(graph, i, 'win')
        dfs(graph, i, 'lose')
        answer += (len(visited) == n)

    return answer

if __name__ == '__main__':
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))