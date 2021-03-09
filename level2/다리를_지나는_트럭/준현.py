from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length
    bridge = deque(bridge)
    truck_weights.reverse()
    sum_bridge = 0
    while truck_weights:
        if weight < truck_weights[0]:
            return answer
        if sum_bridge-bridge[0]+truck_weights[-1] <= weight:
            now_truck = truck_weights.pop()
            bridge += [now_truck]
            sum_bridge += now_truck
        else:
            bridge += [0]
        answer += 1
        sum_bridge -= bridge.popleft()
    if sum(bridge) != 0:
        bridge.reverse()
        for i in bridge:
            if i != 0:
                count = len(bridge)-bridge.index(i)
                break
    return answer+count