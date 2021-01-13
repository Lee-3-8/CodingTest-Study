# 찾아라 프로그래밍 마에스터    폰켓몬
def solution(nums):
    select_num = len(nums) // 2
    nums = set(nums)
    nums_len = len(nums)
    return min(nums_len, select_num)


# nums = [3, 1, 2, 3]
# nums = [3,3,3,2,2,4]
nums = [3, 3, 3, 2, 2, 2]
print(solution(nums))