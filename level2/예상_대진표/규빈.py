import math
def solution(n,a,b):
    maxNum = int(math.log2(n))
    std = 0
    for i in range(maxNum, 0, -1):
        std += n//2
        flagA = up(std, a)
        flagB = up(std, b)
        if flagA == flagB:
            if flagA is False:
                std -= n//2

        else:
            return i
        n = n//2

def up(halfN, num):
    return num > halfN