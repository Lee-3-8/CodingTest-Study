from collections import defaultdict


def solution(n, results):
    gp = [[0] * (n + 1) for i in range(n + 1)]
    for w, l in results:
        gp[w][l] = 1
        gp[l][w] = -1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if gp[i][j] == 1:
                for q in range(1, n + 1):
                    if i != q and gp[j][q] == 1:
                        gp[i][q] = 1
                        gp[q][i] = -1

            elif gp[i][j] == -1:
                for q in range(1, n + 1):
                    if i != q and gp[j][q] == -1:
                        gp[i][q] = -1
                        gp[q][i] = 1

    cnt = 0
    for i in range(1, n + 1):
        flag = 0
        for j in range(1, n + 1):
            if i != j and gp[i][j] == 0:
                flag = 1
                break
        if flag == 0:
            cnt += 1

    return cnt


if __name__ == "__main__":
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
