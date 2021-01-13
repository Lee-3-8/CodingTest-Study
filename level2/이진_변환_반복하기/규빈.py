def solution(s):
    answer = [0, 0]

    while(s != "1"):
        s, answer = binaryChange(s, answer)

    return answer


def binaryChange(s, answer):
    numOne = sum(int(i) for i in s)
    cutZero = len(s) - numOne
    answer[0] += 1
    answer[1] += cutZero
    toBinary = format(numOne, 'b')
    return toBinary, answer