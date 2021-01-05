def solution(n, arr1, arr2):
    pattern = [' ', '#']
    result = []
    for i in range(n) :
        decoded = ''
        union = arr1[i] | arr2[i]
        for _ in range(n):
            decoded = pattern[union % 2] + decoded
            union //= 2
        result.append(decoded)
    
    return result


if __name__ == '__main__':
    result = solution(
        6,
        [46, 33, 33 ,22, 31, 50],
        [27 ,56, 19, 14, 14, 10]
    )
    print(result)