def solution(numbers):
    answer = []
    for n in numbers:
        bi = format(n, 'b')
        length = len(bi)
        idx = bi.rfind('0')
        if idx < 0:
            answer.append(2**length + n - 2**(length-1))
        elif idx < length-1:
            answer.append(n + 2**(length-1-idx) - 2**(length-1-idx-1))
        else:
            answer.append(n + 1)
    return answer