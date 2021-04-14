# 3레벨     코딩테스트 고득점 Kit     등굣길
def solution(m, n, puddles):
    gp = [[0] * (m + 1) for _ in range(n + 1)]
    gp[1][1] = 1
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if x == y == 1:
                continue
            if [x, y] not in puddles:
                gp[y][x] = gp[y - 1][x] + gp[y][x - 1]

    print(gp)
    return gp[n][m] % 1000000007


if __name__ == "__main__":
    print(solution(4, 3, [[2, 2]]))
