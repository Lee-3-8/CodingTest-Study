def solution(n, costs, answer=0):
    change = lambda x: node[src] if x == ex_node else x
    node = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])

    for src, dst, point in costs:
        if len(set(node)) == 1:
            return answer
        elif node[src] != node[dst]:
            ex_node = node[dst]
            node = list(map(change, node))
            answer += point

    return answer

if __name__ == '__main__':
    print((solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,8],[2,3,1]])))