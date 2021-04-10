

def solution(triangle):
    l = len(triangle)
    for i in range(1, l):
        ll = len(triangle[i])
        for j in range(ll):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == ll-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(solution(triangle))
