# SummerWinter Coding(~2018)    소수 만들기
# itertools의 combinations를 이용해 리스트에서 조합을 뽑아 쉽게 풀 수있음 (ex. 10개에서 3개를 뽑을때 조합 (중복X) )
# 소수 판별 필요
from itertools import combinations

# 파이썬닉한 버전
def solution(nums):
    prime_num = 0
    prime_num += sum([is_prime(sum(x)) for x in list(combinations(nums, 3))])
    return prime_num


# 꼼수 버전
def solution1(nums):
    nums_len = len(nums)
    two_arr = []
    triple_arr = []
    prime_num = 0

    for i in range(nums_len):
        for j in range(i + 1, nums_len):
            two_arr.append([nums[i], nums[j]])

    for arr in two_arr:
        for num in nums:
            if num not in arr:
                prime_num += is_prime(sum(arr) + num)

    print(two_arr)
    return prime_num // 3


def is_prime(num):
    """소수 체크 함수
    return: 1 -> 소수 , 0 -> 소수X
    """
    for i in range(2, num):
        if num % i == 0:
            return 0

    return 1


"""
예시 출력
"""
# nums = [1, 2, 3, 4]
nums = [1, 2, 7, 6, 4]
print(solution(nums))