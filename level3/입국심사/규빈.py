def solution(n, times):
    left = 0
    right = times[-1] * n
    while left < right :
        left, right = binarySearch(left, right, n, times)
    return left

def binarySearch(left, right, n, times):
    mid = (left + right)//2
    cnt = 0

    for time in times:
        cnt += mid//time

    if cnt >= n:
        return left, mid
    else:
        return mid+1, right