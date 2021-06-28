from collections import deque

def refind_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                board[i][j] = {}

def solution(board):
    refind_board(board)
    n, q = len(board), deque([(0, 0, 0, 0), (0, 0, 0, 1)])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while q:
        x, y, cost, pre_dir = q.popleft()
        for i, (dx, dy) in enumerate(dirs):
            nx, ny = x + dx, y + dy
            ncost = cost + (600 if pre_dir != i else 100)
            if (
                (0 <= nx < n and 0 <= ny < n)
                and board[nx][ny] != 1
            ):
                if i not in board[nx][ny] or ncost < board[nx][ny][i]:
                    board[nx][ny][i] = ncost
                    q.append((nx, ny, ncost, i))

    return min(board[-1][-1].values())