# 2레벨     코딩테스트 고득점 Kit     다리를 지나는 트럭
from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    ing = deque()
    time = 0
    while ing or truck_weights:
        time += 1
        if ing and time - ing[0][1] == bridge_length:
            weight += ing.popleft()[0]

        if truck_weights and weight >= truck_weights[0]:
            truck = truck_weights.popleft()
            weight -= truck
            ing.append([truck, time])

        # print(time, ing)
    return time


if __name__ == "__main__":
    print(solution(2, 10, [7, 4, 5, 6]))
