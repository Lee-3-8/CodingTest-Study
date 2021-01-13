import re

def solution(s):
    answer = []
    nums = [] # 모든 숫자
    numNum = [] # 각 숫자의 갯수

    num = re.compile(r'\d+')
    strNums = num.findall(s)

    for i in strNums:
        nums.append(int(i))
    numOnly = list(set(nums)) # 모든 숫자가 1개씩 있음

    Length = len(numOnly)
    
    for i in range(Length) :
        numNum.append(nums.count(numOnly[i]))

    for _ in range(Length) :
        idx = numNum.index(max(numNum))
        answer.append(numOnly[idx])
        numNum[idx] = 0

    return answer