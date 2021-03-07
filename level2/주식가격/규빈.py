from collections import deque
def solution(prices):
    result = deque([])

    for i in range(len(prices)-1,-1,-1):
        if i == len(prices) -1 :
            result.appendleft(0)
            continue
        
        cnt = 0
        for j in range(i+1,len(prices)):
            if prices[i] > prices[j]:
                cnt += 1
                break
            cnt += 1

        result.appendleft(cnt)
    return list(result)