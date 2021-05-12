

def find(a, parent):
    if a == parent[a]:
        return a

    parent[a] = find(parent[a], parent)
    return parent[a]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, computers):
    parent = [0]*n
    for i in range(n):
        parent[i] = i
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                union(i, j, parent)
    answer = n
    for i in range(n):
        if i != find(i, parent):
            answer -= 1
    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))
