import math
n = 8
a = 1
b = 4


def solution(n, a, b):
    pow = int(math.log2(n))
    if (a-1)//2 == (b-1)//2:
        return 1
    if a > b:
        a, b = b, a
    n /= 2
    plus = n
    while True:
        print(a, b)
        if a <= n and b > n:
            return pow
        elif a <= n and b <= n:
            pow -= 1
            plus /= 2
            n -= plus
        else:
            pow -= 1
            plus /= 2
            n += plus


print(solution(n, a, b))
