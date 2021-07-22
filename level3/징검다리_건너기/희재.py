def is_available(stones, mid, k):
    cnt = 0
    for stone in stones:
        if stone <= mid:
            cnt += 1
        else:
            cnt = 0
        if cnt >= k:
            return False
    return True

def solution(stones, k):
    left, right = 1, 200_000_000
    while left <= right:
        mid = (left + right) // 2
        if is_available(stones, mid, k):
            left = mid + 1
        else:
            right = mid - 1
    return left

if __name__ == '__main__':
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))


