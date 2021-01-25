def solution(m, n, board):
    answer = 0
    arr = [[board[i][j] for i in range(m-1, -1, -1)] for j in range(n)] # 오른쪽 회전
    flag = True
    while(flag):
        flag = False
        a = set() # 터트릴 좌표
        for i in range(n-1):
            for j in range(m-1):
                if arr[i][j] == '0': # 이후 볼 필요 x
                    break
                if isSame(i,j,arr):
                    a.add((i,j))
                    a.add((i,j+1))
                    a.add((i+1,j))
                    a.add((i+1,j+1))
        answer += len(a)
        flag = allPop(n,m,arr,a)
    return answer

def isSame(row,col,arr):
    if row == len(arr)-1 or col == len(arr[0])-1:
        return False
    ch = arr[row][col]
    if arr[row+1][col] == ch:
        if arr[row][col+1] == ch:
            if arr[row+1][col+1] == ch:
                return True
    return False

def allPop(row,col,arr,a):
    flag = False
    for i in range(row):
        cnt = 0
        for j in range(col-1, -1, -1):
            if (i,j) in a:
                arr[i].pop(j)
                cnt += 1
                flag = True
        b = ['0' for k in range(cnt)]
        arr[i].extend(b)
    return flag