from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
def dfs(temp,grid,visited):
    # x y z
    L={0:[1,0,3],1:[0,1,0],2:[-1,0,1],3:[0,-1,2]}
    R={0:[-1,0,1],1:[0,-1,2],2:[1,0,3],3:[0,1,0]}
    S={0:[0,1,0],1:[1,0,1],2:[0,-1,2],3:[-1,0,3]}
    row=len(grid)
    column=len(grid[0])
    queue=deque()
    queue.append(temp)
    cnt=0
    now_visited=set()
    while queue:
        y,x,z=queue.popleft()
        y%=row
        x%=column
        if (y,x,z) in now_visited:
            visited|=now_visited
            return cnt
        if (y,x,z) in visited:
            return False
        now_visited.add((y,x,z))
        if grid[y][x]=='L':
            cnt+=1
            queue.append((y+L[z][1],x+L[z][0],L[z][2]))
        elif grid[y][x]=='R':
            queue.append((y+R[z][1],x+R[z][0],R[z][2]))
            cnt+=1
        else:
            queue.append((y+S[z][1],x+S[z][0],S[z][2]))
            cnt+=1
        
    return cnt


# 0 위 1 오 2 아래 3 왼
def solution(grid):
    answer = []
    visited=set()
    row=len(grid)
    column=len(grid[0])
    for i in range(row):
        for j in range(column):
            for k in range(4):
                count=dfs((i,j,k),grid,visited)
                if count:
                    answer.append(count)
    return sorted(answer)

print(solution([["SRSRLRRSRR"],["SSRLRRRRSRR"],["SRSRRLLSRR"]]))
