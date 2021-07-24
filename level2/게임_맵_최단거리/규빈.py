from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([[0,0]])
    dirX, dirY = [0,1,0,-1], [1,0,-1,0] # 하, 우, 상, 좌
    
    while queue:
        cur = queue.popleft()

        for i in range(4):
            nodeX, nodeY = cur[0] + dirX[i], cur[1] + dirY[i]
            if 0 <= nodeX < m and 0 <= nodeY < n:
                if maps[nodeY][nodeX] == 1 or maps[nodeY][nodeX] > maps[cur[1]][cur[0]] + 1:
                    maps[nodeY][nodeX] = maps[cur[1]][cur[0]] + 1
                    queue.append([nodeX,nodeY])

    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1