def solution(prices):
    result = []
    for i in range(len(prices)-1):
        temp =len(prices) - i -1
        for j in range(i+1,len(prices)):
            if prices[j] < prices[i]:
                temp = j - i
                break
        result.append(temp)
    result.append(0)
    return result

print(solution(	[1, 2, 3, 2, 3]))
