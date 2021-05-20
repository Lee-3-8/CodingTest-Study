

def solution(n, times):
    if n == 0:
        return 0
    times.sort()
    left = 1
    right = (len(times)+1)*times[-1]
    while left <= right:
        print(left, right)
        mid = (left+right)//2
        cnt = 0
        for j in times:
            cnt += mid//j
            if cnt >= n:
                break
        if cnt >= n:
            answer = mid
            right = mid-1
        else:
            left = mid+1
    return answer


n = 6
times = [7, 10]
print(solution(n, times))
