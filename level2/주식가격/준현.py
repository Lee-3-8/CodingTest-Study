
def solution(prices):

    answer = []
    for i in range(len(prices)):
        temp = prices[i]
        count = 0
        for j in range(i+1, len(prices)):
            count += 1
            if temp > prices[j]:
                break
        answer.append(count)
    return answer


prices = [1, 2, 3, 2, 3, 1]

print(solution(prices))
