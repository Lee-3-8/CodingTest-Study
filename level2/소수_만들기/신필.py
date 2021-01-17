from itertools import combinations

def isPrime1(n): # 무식 소수 
	if(n<2):
		return 0
	for i in range(2,n):
		if(n%i==0):
			return 0
	return 1

def isPrime2(n): # 에라토스테네스의 체 
    a = [False,False] + [True]*(n-1)
    primes=[]
    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
    return(primes)


def solution1(nums): # 처음푼거 
    n = len(nums)
    result = 0
    temp = [0,0,0]
    for i in range(n-2):
        temp[0] = nums[i]
        for j in range(i+1,n-1):
            temp[1] = nums[j]
            for k in range(j+1,n):
                temp[2] = nums[k]
                print(sum(temp))
                result += isPrime1(sum(temp))
    return result


def solution2(nums): # 두번째
    re_arr = list(combinations(nums,3))
    re_arr = list(map(lambda x: sum(x) , re_arr))
    result = 0
    for i in re_arr:
        result += isPrime1(i)
    return result

def solution3(nums): # 에라토스테네스의 체 사용
    re_arr = list(combinations(nums,3))
    re_arr = list(map(lambda x: sum(x) , re_arr))
    result = isPrime2(max(re_arr))
    cnt = 0
    for i in re_arr:
        if i in result:
            cnt += 1

    return cnt

print(solution3([1,2,3,4]))
# print(solution([1,2,7,6,4]))