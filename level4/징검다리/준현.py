from itertools import combinations


def solution(distance, rocks, n):
    left = 0
    right = distance
    rocks.append(distance)
    rocks.sort()
    while left <= right:
        print(left, right)
        mid = (left+right)//2
        cnt = 0
        arr = []
        start = mid
        prev = 0
        for i in rocks:
            if i-prev >= start:
                arr.append(i)
                prev = i
            else:
                cnt += 1

        if cnt > n:
            right = mid-1
        else:
            answer = mid
            left = mid+1
    return answer


distance = 25

rocks = [2, 14, 11, 21, 17]
n = 2
print(solution(distance, rocks, n))
