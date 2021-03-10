from collections import deque

def solution(bridge_length, weight, truck_weights):
    wait = deque(truck_weights)
    bridge = deque([[bridge_length, wait.popleft()]])
    cnt = 1
    while bridge:
        cnt += 1
        # 다리에서 시간소모
        for i in range(len(bridge)):
            bridge[i][0] += -1
        # 다리에서 나옴
        if bridge[0][0] == 0:
            bridge.popleft()
        # 들어감
        if wait and (sum(map(lambda x: x[1],bridge)) + wait[0]) <= weight:
            bridge.append([bridge_length, wait.popleft()])

    return cnt

print(solution(	100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))