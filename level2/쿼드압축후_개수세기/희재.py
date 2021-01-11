import numpy as np

def compress(arr, n):
    arr_sum, nn, n2 = arr.sum(), n * n, n // 2
    if arr_sum == nn:
        return np.array([0, 1])
    elif arr_sum == 0:
        return np.array([1, 0])
    else:
        return (
            compress(arr[:n2, :n2], n2) +
            compress(arr[:n2, n2:n], n2) +
            compress(arr[n2:n, :n2], n2) +
            compress(arr[n2:n, n2:n], n2)
        )

def solution(arr):
    answer = compress(np.array(arr), len(arr))
    return list(answer)

if __name__ == '__main__':
    result = solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])
    print(result)