from collections import deque
import sys
sys.setrecursionlimit(10000000)

def solution(maps):
    n, m = len(maps[0]),len(maps)
    move = [(-1,0),(0,-1),(1,0),(0,1)]
    def dfs(a,b):
        for i, j in move:
            x, y = a + i, b + j
            if 0 <= x < n and 0 <= y < m:
                if maps[y][x] == 1 or maps[b][a] + 1 < maps[y][x]:
                        maps[y][x] = maps[b][a] + 1
                        dfs(x,y)

    dfs(0,0)

    return -1 if maps[-1][-1] == 1 else maps[-1][-1]

if __name__ == '__main__':
    print(solution(	[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
    print(solution(		[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
