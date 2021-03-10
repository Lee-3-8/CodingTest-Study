from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length, maxlen=bridge_length)
    bridge_sum = 0

    while bridge or truck_weights:
        bridge_sum -= bridge.popleft()
        if truck_weights and bridge_sum + truck_weights[0] <= weight:
            bridge.append(truck_weights.popleft())
            bridge_sum += bridge[-1]
        elif truck_weights:
            bridge.append(0)
        answer += 1

    return answer

if __name__ == '__main__':
    print(solution(
        2, 10, [7,4,5,6]
    ))