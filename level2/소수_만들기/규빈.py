def solution(nums):
    answer = 0
    Len = len(nums)

    for i in range(Len):
        for j in range(i+1,Len):
            for k in range(j+1,Len):
                if isPrime(nums[i], nums[j], nums[k]):
                    answer += 1

    return answer

def isPrime(num1, num2, num3):
    num = num1 + num2 + num3
    cnt = 0
    for i in range(2, num + 1):
        if num % i == 0:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

print(solution([1,2,7,6,4]))