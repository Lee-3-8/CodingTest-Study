from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    truck_weights = deque(truck_weights)
    bridge = deque(bridge)
    sumBridge = 0
    
    while truck_weights or sumBridge:
        if truck_weights and sumBridge + truck_weights[0] <= weight:
            bridge.appendleft(truck_weights.popleft())
        else:
            bridge.appendleft(0)
        bridge.pop()

        sumBridge += bridge[0] - bridge[bridge_length-1]
        answer += 1

    return answer + 1