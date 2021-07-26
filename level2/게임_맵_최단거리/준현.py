from collections import deque

def solution(maps):
    m=len(maps)
    n=len(maps[0])
    answer=[[0] * n  for i in range(m)]
    nx=[1,-1,0,0]
    ny=[0,0,1,-1]
    queue=deque()
    queue.append((0,0,0))
    while queue:
        y, x,z = queue.popleft()
        if y== m-1 and x==n-1:
            return answer[m-1][n-1]+1
        for i in range(4):
            dx=nx[i]+x
            dy=ny[i]+y
            if 0<=dx<n and 0<=dy<m  and maps[dy][dx]==1:
                if answer[dy][dx] ==0 or answer[dy][dx]>z+1:
                    answer[dy][dx]=z+1
                    queue.append((dy,dx,z+1))
    return -1


maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

print(solution(maps))