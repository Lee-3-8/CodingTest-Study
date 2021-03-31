

# def solution(n, costs):
#     nodes = [set([i]) for i in range(n)]
#     e_cnt, result = 0, 0
#     for i in sorted(costs,key = lambda x:x[2]):
#         print(i,nodes)
#         if e_cnt == n-1: break
#         if not(nodes[i[0]] & nodes[i[1]]):
#             e_cnt += 1
#             result += i[2]
#             nodes[i[0]] = nodes[i[0]] | nodes[i[1]]
#             nodes[i[1]] = nodes[i[0]]
#             #union nodes
#     print(nodes)
#     return result


def solution(n, costs):
    nodes = [i for i in range(n)]
    result = [0,0]
    for i in sorted(costs,key = lambda x:x[2]):
        if result[0] == n-1: break
        if nodes[i[0]] != nodes[i[1]]: # 최상위부모노드가 같지 않은 경우에만 연결
            result[0] += 1
            result[1] += i[2]
            nodes = list(map(lambda x: nodes[i[1]] if x == nodes[i[0]] else x,nodes))
            #union nodes
    print(nodes)
    return result[1]

print(solution(	4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
# print(solution1(	5,[[0,1,1],[0,2,2],[1,2,5],[2,3,8],[3,4,1]]))
# print(solution(	2, [[0,1,1]]))
