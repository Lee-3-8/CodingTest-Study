def solution(prices):
    answer, stack = [0] * len(prices), []
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            answer[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)

    for i in range(len(stack)):
        answer[stack[i]] = len(prices) - stack[i] - 1

    return answer

if __name__ == '__main__':
    print(solution([2, 1]))


"""
def solution(prices):
    result=[]
    for i, v in enumerate(prices):
        cnt=0
        for j in range(i+1, len(prices)):
            if v>prices[j]:
                cnt+=1
                break
            else:
                cnt+=1
        result.append(cnt)
    return result
"""