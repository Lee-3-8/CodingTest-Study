from collections import deque

def solution(maps):
    q = deque([(0, 0)])
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    n, m = len(maps), len(maps[0])
    while q:
        x, y = q.popleft()
        for i, j in dir:
            next_x, next_y = x + i, y + j
            if 0 <= next_x < n and 0 <= next_y < m:
                if maps[next_x][next_y] != 0:
                    if (
                        maps[next_x][next_y] == 1
                        or maps[x][y] + 1 < maps[next_x][next_y]
                    ):
                        maps[next_x][next_y] = maps[x][y] + 1
                        q.append((next_x, next_y))

    return -1 if maps[-1][-1] == 1 else maps[-1][-1]

if __name__ == '__main__':
    print(solution((
        [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])))
    print(solution(
        [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
    ))