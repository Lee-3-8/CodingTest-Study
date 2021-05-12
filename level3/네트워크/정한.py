# 3레벨     코딩테스트 고득점 Kit     네트워크


def solution(n, computers):
    parent = [i for i in range(0, n + 1)]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    def find(a):
        if a == parent[a]:
            return a
        parent[a] = find(parent[a])
        return parent[a]

    for idx, com in enumerate(computers):
        for i in range(0, n):
            if idx == i:
                continue
            if com[i] == 1 and find(idx + 1) != find(i + 1):
                union(idx + 1, i + 1)
    for i in range(1, n + 1):
        find(i)
    parent = set(parent[1:])
    return len(parent)


if __name__ == "__main__":
    # print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    # print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
    # print(solution(2, [[1, 1], [0, 1]]))
    print(
        solution(
            5, [[1, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1], [1, 0, 0, 0, 1]]
        )
    )
