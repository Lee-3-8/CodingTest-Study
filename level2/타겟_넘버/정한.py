# 2레벨     코딩테스트 고득점 Kit     타겟 넘버

cnt = 0


def solution(numbers, target):
    def re(idx, sym, sum):
        global cnt
        # print("실행")
        if sym == "+":
            sum += numbers[idx]
        else:
            sum -= numbers[idx]

        if idx == len(numbers) - 1:
            if sum == target:
                cnt += 1
            return
        re(idx + 1, "-", sum)
        re(idx + 1, "+", sum)

    re(0, "-", 0)
    re(0, "+", 0)

    return cnt


if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))
