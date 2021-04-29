# 4레벨     코딩테스트 고득점 Kit     도둑질
def solution(money):
    _max1 = [0] * len(money)
    _max2 = [0] * len(money)

    _max1[0] = money[0]
    _max1[1] = max(money[0], money[1])
    for idx in range(2, len(money) - 1):
        _max1[idx] = max(_max1[idx - 2] + money[idx], _max1[idx - 1])

    
    _max2[0] = 0
    _max2[1] = money[1]
    for idx in range(2, len(money)):
        _max2[idx] = max(_max2[idx - 2] + money[idx], _max2[idx - 1])

    return max(_max1[-2], _max2[-1])


if __name__ == "__main__":
    print(solution([1, 2, 3, 1]))