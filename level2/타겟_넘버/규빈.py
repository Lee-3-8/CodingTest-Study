def solution(numbers, target):
    turn = 0
    return dfs(numbers,target,turn)

def dfs(numbers, target, turn):
    if turn == len(numbers):
        return 1 if sum(numbers)==target else 0
    a = dfs(numbers,target,turn+1)
    numbers[turn] = numbers[turn] * -1
    b = dfs(numbers,target,turn+1)
    return a + b