def solution(key, lock):
    lpiece, row, col = pieceOfArray(lock, 0)
    kpiece, krow, kcol = pieceOfArray(key, 1)

    if not lpiece: # 홈이 없는 경우
        return True

    for i in range(krow):
        for j in range(kcol):
            kpiece[i][j] = abs(kpiece[i][j] - 1)
                
    for _ in range(4):
        if isMatch(kpiece, lpiece):
            return True
        lpiece = rotateArr(lpiece, row, col)
        row, col = col, row

    return False

def pieceOfArray(arr, flag): # 최소 조각 자르기
    minRow = minCol = lenA = len(arr)
    maxRow = maxCol = 0
    for i in range(lenA):
        for j in range(lenA):
            if arr[i][j] == flag:
                minRow, minCol = min(minRow, i), min(minCol, j)
                maxRow, maxCol = max(maxRow, i), max(maxCol, j)
    arr = [[arr[i][j] for j in range(minCol, maxCol + 1)] for i in range(minRow,maxRow+1)]
    return arr, maxRow - minRow + 1, maxCol - minCol + 1


def rotateArr(arr, row, col): # 시계 방향으로 90도 회전
    arr2 = [[arr[i][j] for i in range(row-1, -1, -1)] for j in range(col)]
    return arr2

def isMatch(key, lock): # 맞춰보기
    kRow, kCol = len(key), len(key[0])
    lRow, lCol = len(lock), len(lock[0])
    if lRow > kRow or lCol > kCol:
        return False
    for i in range(kRow - lRow + 1):
        for j in range(kCol - lCol + 1):
            flag = True
            for k in range(lRow):
                if key[i+k][j:j+lCol] != lock[k]:
                    flag = False
            if flag:
                return True