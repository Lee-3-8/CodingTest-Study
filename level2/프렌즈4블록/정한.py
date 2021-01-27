# 2018 KAKAO BLIND RECRUITMENT      [1차] 프렌즈4블록


def solution(m, n, board):
    answer = 0
    temp = []

    # 1차원 배열 -> 2차원배열로 변환
    for i in board:
        temp.append(list(i))
    while 1:
        idx_list = fun_del(m, n, temp)  # 칸 지우기
        if len(idx_list) == 0:  # 지운게 없으면 완료
            break
        fun_full(m, n, temp, idx_list)  # 빈칸 끌어당기기
    return sum(temp, []).count(0)


def fun_del(m, n, temp):
    idx_list = []
    for i in range(m - 1):
        for j in range(n - 1):
            c = temp[i][j]
            if c != 0 and c == temp[i + 1][j] and c == temp[i][j + 1] and c == temp[i + 1][j + 1]:
                idx_list.append([i, j])
                idx_list.append([i + 1, j])
                idx_list.append([i, j + 1])
                idx_list.append([i + 1, j + 1])
    for i in idx_list:
        temp[i[0]][i[1]] = 0

    return idx_list


def fun_full(m, n, temp, idx_list):
    for j in range(n - 1, -1, -1):
        for i in range(m - 1, -1, -1):
            if temp[i][j] == 0:
                for q in range(i - 1, -1, -1):
                    if temp[q][j] != 0:  # swap
                        temp[i][j], temp[q][j] = temp[q][j], temp[i][j]
                        break


"""
입출력 예시
"""
m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m, n, board))
