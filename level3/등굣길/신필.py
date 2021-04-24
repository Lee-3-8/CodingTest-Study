def solution(m, n, puddles):
    dp = [[0] * m for i in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if [j + 1, i + 1] in puddles:
                dp[i][j] = 0
            else:
                if i != 0:
                    dp[i][j] += dp[i - 1][j]
                if j != 0:
                    dp[i][j] += dp[i][j - 1]
    return dp[n - 1][m - 1] % 1000000007


if __name__ == "__main__":
    print(solution(4, 3, [[2, 2], [1, 2]]))
    # print(solution(4, 3, [[]]))
    # print(solution(3, 2, [[]]))