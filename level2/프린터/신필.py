
# def solution(priorities, location):
#     cnt = 0
#     for i in range(location):
#         if priorities[i] < priorities[location]:
#             cnt += 1
#     for i in range(location + 1,len(priorities)):
#         if priorities[i] > priorities[location]:
#             cnt -= 1

#     return location + 1 - cnt


# 1,1,9,3,5,7

# from collections import deque

# def rolling(deq,location):
#     for i in range(deq):
#         if deq[i] > deq[location]

# def solution(priorities, location):
#     deq = deque(priorities)
#     return rolling(deq,location)

# solution([1,2],3)

from collections import deque

def solution(priorities, location):
    deq = deque(priorities)
    max_i = max(deq)
    cnt = 0
    while True:
        top = deq.popleft()
        if top == max_i:
            cnt += 1
            if location == 0:
                return cnt
            else:
                location -= 1
                max_i = max(deq)
        else:
            deq.append(top)
            if location == 0:
                location = len(deq) - 1
            else:
                location -= 1
    return None

print(solution(		[2, 1, 3, 2], 2))