def solution(maps):
    n, m = len(maps[0]),len(maps)
    for y in range(m):
        for x in range(n):
            if maps[y][x] == 1: maps[y][x] = float('inf')

    def dfs(a,b):
        if maps[-1][-1] != 1 and maps[b][a] >= maps[-1][-1] : return
        move = [(-1,0),(0,-1),(1,0),(0,1)]
        for i, j in move:
            x, y = a + i, j + b
            if 0 <= x < n and 0 <= y < m:
                if maps[y][x] != 0:
                    if maps[b][a] + 1 < maps[y][x]:
                        maps[y][x] = maps[b][a] + 1
                        dfs(x,y)
    maps[0][0] = 1
    dfs(0,0)
    return -1 if maps[-1][-1] == float('inf') else maps[-1][-1]

if __name__ == '__main__':
    print(solution(	[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
    print(solution(		[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
