# 2020 카카오 인턴십    키패드 누르기


def distance_check(target, l_locatin, r_locatin, hand):
    # 피타고라스 공식으로 실제 거리를 계산했음 -> 문제에서는 대각의 길이을 루트2가 아닌 그냥 2로 취급하고 계산함
    # l_distance = (abs(l_locatin[0] - target[0]) ** 2 + abs(l_locatin[1] - target[1]) ** 2) ** 0.5
    # r_distance = (abs(r_locatin[0] - target[0]) ** 2 + abs(r_locatin[1] - target[1]) ** 2) ** 0.5

    l_distance = abs(l_locatin[0] - target[0]) + abs(l_locatin[1] - target[1])
    r_distance = abs(r_locatin[0] - target[0]) + abs(r_locatin[1] - target[1])

    if l_distance == r_distance and hand == "left" or l_distance < r_distance:
        l_locatin[0] = target[0]
        l_locatin[1] = target[1]
        result = "L"

    else:
        r_locatin[0] = target[0]
        r_locatin[1] = target[1]
        result = "R"

    return l_locatin, r_locatin, result


def solution(numbers, hand):
    answer = ""
    keypad = {
        "1": [0, 0],
        "2": [0, 1],
        "3": [0, 2],
        "4": [1, 0],
        "5": [1, 1],
        "6": [1, 2],
        "7": [2, 0],
        "8": [2, 1],
        "9": [2, 2],
        "*": [3, 0],
        "0": [3, 1],
        "#": [3, 2],
    }
    l_locatin = keypad["*"]
    r_locatin = keypad["#"]

    for num in numbers:
        target = keypad[str(num)]
        if num == 1 or num == 4 or num == 7:
            l_locatin[0] = target[0]
            l_locatin[1] = target[1]
            result = "L"

        elif num == 3 or num == 6 or num == 9:
            r_locatin[0] = target[0]
            r_locatin[1] = target[1]
            result = "R"

        else:
            l_locatin, r_locatin, result = distance_check(target, l_locatin, r_locatin, hand)
        answer = answer + result

    return answer


"""
출력 확인
"""
# # numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# # numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# numbers = [2, 1, 3, 4, 5, 6, 7, 8, 9, 0]
# hand = "right"
# # hand = "left"

# print(solution(numbers, hand))
