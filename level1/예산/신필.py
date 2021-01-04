
def solution(d, budget):
    d.sort()
    sum = 0
    for i,v in enumerate(d):
        sum += v
        print(i, sum)
        if sum > budget:
            return i
    return len(d)

print(solution([1,3,2,5,4], 9))
