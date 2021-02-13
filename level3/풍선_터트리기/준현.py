def solution(a):
    if len(a) <= 2:
        return len(a)

    answer = len(a)
    left_min = a[0]
    right = float('inf')
    right_list = [0 for _ in range(len(a))]
    for i in range(len(a)-1, -1, -1):
        if right > a[i]:
            right = a[i]
        right_list[i] = right
    for i in range(len(a)):
        if left_min > a[i]:
            left_min = a[i]

        if left_min < a[i] and right_list[i] < a[i]:
            print(a[i])
            answer -= 1
    return answer
