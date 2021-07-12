from collections import deque
import sys
sys.setrecursionlimit(2500)

def check(ny , nx,size,board):
    if 0<= nx < size and 0<= ny < size and board[ny][nx]==0:
        return True
    else:
        return False
def mincheck(ny,nx,checked,result):
    if checked[ny][nx]== 0 or checked[ny][nx] > result:
        return True
    else:
        return False

def solution(board):
    size= len(board)
    queue=deque()
    queue.append((0,0,0,0)) # x축으로 이동 1 y 축으로 이동 -1
    checked=[[0] * size for i in range(size)]
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    answer= float('inf')
    while queue:
        axis , y , x , result= queue.popleft()
        if y== size-1 and x== size-1 and answer>result:
            answer=result
        for i in range(4):
            nx=dx[i] + x 
            ny=dy[i] + y
            if check(ny,nx,size,board) and mincheck(ny,nx,checked,result):
                if 0<= i<=1 :
                    if axis== -1:
                        checked[ny][nx]=result+600
                        queue.append((1,ny,nx,checked[ny][nx]))
                    else:
                        checked[ny][nx]=result+100
                        queue.append((1,ny,nx,checked[ny][nx]))
                else:
                    if axis== 1:
                        checked[ny][nx]=result+600
                        queue.append((-1,ny,nx,checked[ny][nx]))
                    else:
                        checked[ny][nx]=result+100
                        queue.append((-1,ny,nx,checked[ny][nx]))
    return answer


board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]

print(solution(board))