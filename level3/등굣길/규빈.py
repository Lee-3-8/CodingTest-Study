def solution(m, n, puddles):
    arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                arr[i][j] = 1
            elif [j+1,i+1] in puddles:
                continue
            else:
                arr[i][j] = (arr[i][j-1] + arr[i-1][j]) % 1000000007

    return arr[n-1][m-1]