def get_distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


def solution(numbers, hand):
    phone = {}
    k = 1
    for i in range(3):
        for j in range(3):
            phone[k] = [i, j]
            k += 1
    phone[0] = [3, 1]
    left_hand = [3, 0]
    right_hand = [3, 2]
    left_number = [1, 4, 7]
    right_number = [3, 6, 9]
    answer = ""
    for i in numbers:
        if i in left_number:
            left_hand = phone[i]
            answer += "L"
        elif i in right_number:
            right_hand = phone[i]
            answer += "R"
        else:
            left_distance = get_distance(left_hand, phone[i])
            right_distance = get_distance(right_hand, phone[i])
            if left_distance < right_distance:
                left_hand = phone[i]
                answer += "L"
            elif left_distance > right_distance:
                right_hand = phone[i]
                answer += "R"
            else:
                if hand == "left":
                    left_hand = phone[i]
                    answer += "L"
                else:
                    right_hand = phone[i]
                    answer += "R"
    return answer
