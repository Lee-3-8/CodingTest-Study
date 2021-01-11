def solution(nums):
    numLength = len(nums)
    length = numLength // 2
    dic = {}
    for i in range(numLength) :
        x = nums[i]
        dic[x] = nums.count(x)
    dicLength = len(dic.keys())
    if dicLength >= length:
        return length
    else :
        return dicLength
