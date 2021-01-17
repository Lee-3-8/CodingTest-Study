from itertools import combinations

def isPrime(n):
	if(n<2):
		return 0
	for i in range(2,n):
		if(n%i==0):
			return 0
	return 1

# def solution(nums):
#     n = len(nums)
#     result = 0
#     temp = [0,0,0]
#     for i in range(n-2):
#         temp[0] = nums[i]
#         for j in range(i+1,n-1):
#             temp[1] = nums[j]
#             for k in range(j+1,n):
#                 temp[2] = nums[k]
#                 print(sum(temp))
#                 result += isPrime(sum(temp))
#     return result


def solution(nums):
    re_arr = list(combinations(nums,3))
    re_arr = list(map(lambda x: sum(x) , re_arr))
    result = 0
    for i in re_arr:
        result += isPrime(i)
    return result
print(solution([1,2,3,4]))
# print(solution([1,2,7,6,4]))