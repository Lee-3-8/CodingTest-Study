def solution(m, n, puddles):
    pad = [[0 for _ in range(m+1)] for _ in range(n+1)]
    puddles = {(j, i) for i, j in puddles}
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                pad[i][j] = 1
            elif (i, j) not in puddles:
                pad[i][j] = pad[i-1][j] + pad[i][j-1]
    return pad[-1][-1] % 1_000_000_007

if __name__ == '__main__':
    print(solution(4,4,[[2,3], [4,2]]))