def solution(stones, k):
    answer = 0
    l, r = 0, max(stones)
    
    while l <= r :
        cross = 0
        mid = (l+r)//2
        for stone in stones:
            if stone < mid:
                cross += 1
                if cross == k:
                    break
            else:
                cross = 0
        if k == cross:
            r = mid - 1
        else:
            answer = max(answer, mid)
            l = mid + 1
    return answer