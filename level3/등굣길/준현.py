

def solution(m, n, puddles):
    answer = 0
    arr = [[0]*m for _ in range(n)]
    for j, i in puddles:
        arr[i-1][j-1] = -1
    for i in range(n):
        if arr[i][0] == -1:
            break
        else:
            arr[i][0] = 1
    for j in range(m):
        if arr[0][j] == -1:
            break
        else:
            arr[0][j] = 1
    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j] != -1:
                if arr[i-1][j] == -1:
                    arr[i][j] = arr[i][j-1]
                elif arr[i][j-1] == -1:
                    arr[i][j] = arr[i-1][j]
                else:
                    arr[i][j] = arr[i-1][j]+arr[i][j-1]

    return arr[n-1][m-1]


m, n, puddles = 4, 3, [[1, 3], [3, 1]]
print(solution(m, n, puddles))
