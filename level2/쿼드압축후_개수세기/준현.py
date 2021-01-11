import numpy as np


def recursive(arr, length):
    if 1 in arr and 0 not in arr:
        return [1]
    elif 0 in arr and 1 not in arr:
        return [0]
    else:
        length //= 2
        first = arr[:length, :length]
        second = arr[:length, length:]
        third = arr[length:, :length]
        four = arr[length:, length:]
        answer = recursive(first, length)+recursive(second, length) + \
            recursive(third, length)+recursive(four, length)
        return answer


def solution(a):
    arr = np.array(a)
    answer = recursive(arr, len(arr))
    return [answer.count(0), answer.count(1)]
