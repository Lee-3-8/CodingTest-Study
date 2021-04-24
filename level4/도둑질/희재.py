def solution(money):
    dp = [money[0], max(money[0], money[1])]
    for i in range(2, len(money) - 1):
        dp.append(max(dp[i-1], dp[i-2] + money[i]))

    dp2 = [0, money[1]]
    for i in range(2, len(money)):
        dp2.append(max(dp2[i - 1], dp2[i - 2] + money[i]))
    return max(dp[-1], dp2[-1])

if __name__ == '__main__':
    print(solution([1,2,3,1]))