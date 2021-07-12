# 3레벨     월간 코드 챌린지 시즌2      모두 0으로 만들기
# 특정 노드에서 dfs를 통해 끝까지 확인한 후 수를 더하면서 시작한 노드에 연산
# 끝에서 부터 연산을 진행해야 쓸데없이 수가 이동하는 부분이 없음
# 재귀가 100만까지 늘려야 통과가 가능함 후에 재귀말고 다른 방식을 이용하면 속도가 빨라질듯
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)


def solution(a, edges):
    tree = defaultdict(list)
    for s, e in edges:
        tree[s].append(e)
        tree[e].append(s)
    visited = [0] * len(a)

    result = 0

    def dfs(node):
        nonlocal result
        visited[node] = 1
        for tnode in tree[node]:
            if not visited[tnode]:
                a[node] += dfs(tnode)
        result += abs(a[node])
        return a[node]

    if sum(a):
        return -1

    dfs(0)
    return result


if __name__ == "__main__":
    print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
