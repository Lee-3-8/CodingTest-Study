from collections import deque
def solution(priorities, location):
    answer = 0
    temp = 0
    priorities = deque(priorities)
    while True:
        temp = priorities[0]
        if temp >= max(priorities):
            if location == 0:
                return answer + 1
            else:
                priorities.popleft()
                location = (len(priorities) + location - 1) % len(priorities)
                answer += 1
        else:
            priorities.popleft()
            priorities.append(temp)
            location = (len(priorities) + location - 1) % len(priorities)
    return answer