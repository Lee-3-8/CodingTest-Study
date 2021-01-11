def solution(nums):
    result = list(set(nums))
    return len(result) if len(result) <= len(nums)//2 else len(nums)//2

print(solution([1,2,2,3,4,1]))