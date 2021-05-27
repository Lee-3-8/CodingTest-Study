def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)

    left, right = 0, distance

    while(left <= right):
        remove = 0
        cur = 0
        mid = (left + right) // 2

        for rock in rocks:
            if rock - cur < mid:
                remove += 1
            else:
                cur = rock
        
        if remove > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid

    return answer