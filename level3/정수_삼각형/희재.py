def solution(tri):
    for i in range(1, len(tri)):
        for j in range(i + 1):
            tri[i][j] = max(
                tri[i-1][j-1] + tri[i][j] if j > 0 else -1,
                tri[i-1][j] + tri[i][j] if j <= i-1 else -1
            )
    return max(tri[-1])

if __name__ == '__main__':
    print(solution([
        [7],
        [3, 8],
        [8, 1, 0],
        [2, 7, 4, 4],
        [4, 5, 2, 6, 5]]
    ))