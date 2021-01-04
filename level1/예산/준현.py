def solution(d, budget):
    d.sort()
    count = 0
    for val in d:
        if budget-val >= 0:
            budget = budget-val
            count += 1
    return count
