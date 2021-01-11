import itertools


def solution(n):
    result = [[0]*i for i in range(1,n+2) ]
    print(result)
    cnt = 1
    x = 0
    y = 0
    for i in range(n):
        for j in range(n-i):
            print(cnt, x, y)
            if i % 3 == 0 :#밑으로
                y += 1
                result[y][x] = cnt
                cnt += 1
            if i % 3 == 1 : #오른쪽으로
                x += 1
                result[y][x] = cnt
                cnt += 1
            if i % 3 == 2 : # 대각선 위로
                y -= 1
                x -= 1
                result[y][x] = cnt
                cnt += 1
    result = sum(result,[])
    result = [i for i in result if i != 0]
    print(result)
    return result

solution(6)