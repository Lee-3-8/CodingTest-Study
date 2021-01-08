# 월간 코드 챌린지 시즌1    삼각 달팽이


def solution(n):
    answer = []
    target = [-1, 0]

    # 초기화
    for i in range(1, n + 1):
        answer.append([0 for _ in range(i)])

    num = 1

    while n > 0:
        # down
        for i in range(0, n):
            target[0] += 1
            answer[target[0]][target[1]] = num
            num += 1
        n -= 1

        # right
        for i in range(0, n):
            target[1] += 1
            answer[target[0]][target[1]] = num
            num += 1
        n -= 1

        # up
        for i in range(0, n):
            target[0] -= 1
            target[1] -= 1
            answer[target[0]][target[1]] = num
            num += 1
        n -= 1

    result = []
    for li in answer:
        result += li

    return result


n = 6
print(solution(n))