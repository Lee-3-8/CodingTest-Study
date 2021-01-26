

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

# m 높이


def solution(m, n, board):
    board = list(map(list, zip(*board)))
    flag = True
    answer = 0
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    while flag is True:
        flag = False
        visited = []
        for i in range(len(board)):
            for j in range(len(board[i])-1):
                flag2 = True
                if 0 < j+1 < len(board[i]) and 0 < i+1 < len(board):
                    for k in range(3):
                        nx = dx[k]+j
                        ny = dy[k]+i
                        if board[i][j] == board[ny][nx] != 0:
                            pass
                        else:
                            flag2 = False
                    if flag2:
                        flag = True
                        visited.append((i, j))
                        for k in range(3):
                            nx = dx[k]+j
                            ny = dy[k]+i
                            visited.append((ny, nx))
        visited = list(set(visited))
        visited.sort(key=lambda x: -x[0])
        for x, y in visited:
            board[x][y] = 0
        # [(5, 1), (5, 2), (4, 1), (4, 2), (2, 3), (2, 2), (1, 2), (1, 1), (1, 3), (0, 1), (0, 2)] 0인거만 뽑기
        for idx in range(len(visited)):
            count = 0
            for i in range(len(board)):
                count = board[i].count(0)
                board[i] = [0]*count+[x for x in board[i] if x != 0]
            answer += 1
    return answer


print(solution(m, n, board))
