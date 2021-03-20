from itertools import permutations


def make_minor(n):
    m = n // 2
    minor = [True]*(n+1)
    for i in range(2, m+1):
        if minor[i]:
            for j in range(i+i, n+1, i):
                minor[j] = False
    a = [i for i in range(2, n+1) if minor[i] == True]
    return a


def solution(numbers):
    answer = 0
    q = list(numbers)
    c = []
    for i in range(1, len(q)+1):
        for j in permutations(q, i):
            c.append("".join(j))

    c = set(map(int, c))
    maxc = max(c)
    print(maxc)
    minor = set(make_minor(maxc))
    print(minor)
    for i in c:
        if i in minor:
            answer += 1
    return answer


numbers = "17"
print(solution(numbers))
