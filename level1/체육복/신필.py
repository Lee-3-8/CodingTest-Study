def solution(n, lost, reserve):
    lost  = set(lost)
    reserve = set(reserve)
    temp = lost & reserve
    lost = lost - temp
    reserve = reserve - temp

    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    return n - len(lost)

print(solution(	5,[2,3,5],[4,3,5]))