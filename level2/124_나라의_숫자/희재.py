def solution(n):
    answer = ""
    length, exp, op = 0, 0, 3
    conv = ["1", "2", "4"]
    while exp < n:
        answer = conv[(n - exp - 1) // (op // 3) % 3] + answer
        exp += op
        op *= 3
    return answer
