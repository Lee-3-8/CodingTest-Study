
def solution(brown, yellow):
    mn = brown+yellow
    mplusn = (yellow-4-mn)//(-2)
    for i in range(1, mplusn):
        m = mplusn-i
        if m*i == mn:
            return [m, i]


brown = 24
yellow = 24

print(solution(brown, yellow))
