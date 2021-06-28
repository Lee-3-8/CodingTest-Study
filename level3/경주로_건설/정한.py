# 2020 카카오 인턴십    경주로 건설
from collections import deque
from copy import deepcopy


def solution(board):
    size = len(board[0])
    visit = [[0] * size for _ in range(size)]
    road = []
    direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # y,x 위 오 아 왼
    result = []

    def bfs(y, x, v, r):
        if y == x == size - 1:
            return road.append(r)
        else:
            for i in range(4):
                dy = y + direct[i][0]
                dx = x + direct[i][1]
                if 0 <= dy < size and 0 <= dx < size and board[dy][dx] == 0 and v[dy][dx] == 0:
                    r.append(direct[i])
                    v[dy][dx] = 1
                    bfs(dy, dx, deepcopy(v), deepcopy(r))
                    r.pop()
                    v[dy][dx] = 0

    bfs(0, 0, deepcopy(visit), deepcopy(road))
    answer = []
    for item in road:
        money = 0
        for i in range(1, len(item)):
            money += 100 if item[i] == item[i - 1] else 500
        answer.append(money)

    print(road)
    print(answer)
    return min(answer)


if __name__ == "__main__":
    print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
