# 상식적으로 큰놈들을 먼저넣고 작은놈들을 조각 넣듯이 넣는게 맞다고 생각
from collections import deque

def solution(people, limit):
    l_boat = 0
    people = deque(sorted(people,reverse=True))
    while people:
        l_boat+=1
        print(people,l_boat)
        if len(people) == 1: break # 큐 크기가 1일때 -1하면 out of range 뜨네
        total = people[0]
        while total + people[-1] <= limit:
            total += people.pop()
        people.popleft()

    return l_boat

print(solution(	[70, 80, 50], 100))