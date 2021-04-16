def solution(money):
    N = len(money)
    DP1 = [0]*(N-1)
    DP2 = [0]*(N)
    DP1[0] = money[0]
    DP1[1] = max(money[0], money[1])
    DP2[1] = money[1]
    DP2[2] = max(money[1], money[2])

    for i in range(2, N-1):
        DP1[i] = max(DP1[i-2]+money[i], DP1[i-1])

    for i in range(3, N):
        print(i)
        DP2[i] = max(DP2[i-2]+money[i], DP2[i-1])

    return DP1[N-2] if DP1[N-2] > DP2[N-1] else DP2[N-1]


money = [1, 2, 3, 1]
print(solution(money))
