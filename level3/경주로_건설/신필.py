
def solution(board):
    n = len(board)
    adjacent = [(1,0),(-1,0),(0,1),(0,-1)]
    def dfs(i,j,acc,last):
        if i == n-1 and j == n-1:
            return 
        for x,y in adjacent:
            if 0 <= x+i < n and 0 <= y+j < n:
                if board[x+i][y+j] != 1:
                    unit = 100 if last[0] + x == 0 or last[1] + y == 0 else 600 #이전 방향과 일치할때 (수직 or 수평이동)
                    if board[x+i][y+j] == 0:
                        board[x+i][y+j] = acc + unit
                        dfs(x+i,y+j,acc+unit,(x,y))
                    else:
                        if board[x+i][y+j] >= acc + unit:
                            board[x+i][y+j] = acc + unit
                            dfs(x+i,y+j,acc+unit,(x,y))

    board[0][0] = 0
    board[0][1] = 100
    board[1][0] = 100

    dfs(0,1,100,(0,1))
    dfs(1,0,100,(1,0))

    return board[n-1][n-1]

if __name__ == '__main__':
    # print(solution(	[[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    # print(solution(	[[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
    print(solution(	[[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
