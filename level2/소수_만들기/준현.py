import sys
from itertools import combinations


def solution(nums):
    arr = list(combinations(nums, 3))
    count = 0
    for i in arr:
        if isDecimal(sum(i)):
            count += 1
    return count


def isDecimal(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


nums = [1, 2, 7, 6, 4]
print(solution(nums))
