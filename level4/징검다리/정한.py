# 4레벨     코딩테스트 고득점 Kit     징검다리


def solution(distance, rocks, n):
    l = 0
    r = distance
    rocks.sort()
    rocks.append(distance)

    while l < r:
        cri = (l + r) // 2
        remove = 0
        last = 0
        best_short = float("inf")

        for rock in rocks:
            if cri >= rock - last:
                remove += 1
            else:
                best_short = min(best_short, rock - last)
                last = rock

        if remove > n:
            r = cri - 1
        else:
            l = cri + 1
            result = best_short

    return result


if __name__ == "__main__":
    print(solution(25, [2, 14, 11, 21, 17], 2))