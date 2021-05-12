def dfs(numbers,index,result,target):
    if len(numbers) == index:
        return 1 if target == result else 0
    
    return dfs(numbers, index+1, result + (numbers[index]*-1),target) + dfs(numbers, index+1, result + (numbers[index]),target)

def solution(numbers, target):
    return dfs(numbers, 1, numbers[0]*-1, target) + dfs(numbers, 1, numbers[0], target)
