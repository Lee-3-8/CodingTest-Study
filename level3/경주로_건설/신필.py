from copy import deepcopy

def arr_print(arr):
    for i in arr:
        for j in i:
            print(j,end=' ')
        print()

def get_min_price(arr,direction):
    n = len(arr)
    adjacent = [(1,0),(-1,0),(0,1),(0,-1)]
    def dfs(i,j,acc,last):
        if i == n-1 and j == n-1:
            return 
        for x,y in adjacent:
            if 0 <= x+i < n and 0 <= y+j < n:
                if arr[x+i][y+j] != 1:
                    unit = 100 if last[0] + x == 0 or last[1] + y == 0 else 600 #이전 방향과 일치할때 (수직 or 수평이동)
                    if arr[x+i][y+j] == 0:
                        arr[x+i][y+j] = acc + unit
                        dfs(x+i,y+j,acc+unit,(x,y))
                    else:
                        if arr[x+i][y+j] >= acc + unit:
                            arr[x+i][y+j] = acc + unit
                            dfs(x+i,y+j,acc+unit,(x,y))

    if direction == 'right':
        dfs(1,0,100,(1,0))
        dfs(0,1,100,(0,1))
    else:
        dfs(0,1,100,(0,1))
        dfs(1,0,100,(1,0))
    return arr[-1][-1]

def solution(board):
    board[0][0] = -1
    board[0][1] = 100
    board[1][0] = 100

    return min(get_min_price(deepcopy(board),'down'),get_min_price(deepcopy(board),'right'))


if __name__ == '__main__':
    # print(solution(   [[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    # print(solution(   [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
    # print(solution(   [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))\
    # print(solution(	[[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]))
    print(solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]))