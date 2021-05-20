# 3레벨     코딩테스트 고득점 Kit     입국심사
def solution(n, times):
    l = 1
    r = min(times) * n
    while l <= r:
        m = (l + r) // 2
        num = 0
        for time in times:
            num += m // time
            if num >= n:
                break

        if num < n:
            l = m + 1
        else:
            r = m - 1

    return l


if __name__ == "__main__":
    print(solution(6, [7, 10]))
