def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    arr = [0, 0, 0]
    result = []
    for idx, val in enumerate(answers):
        if val == a[idx % len(a)]:
            arr[0] += 1
        if val == b[idx % len(b)]:
            arr[1] += 1
        if val == c[idx % len(c)]:
            arr[2] += 1
    max_arr = max(arr)
    for idx, s in enumerate(arr):
        if s == max_arr:
            result.append(idx+1)
    return result


answers = [1, 2, 3, 4, 5]
print(solution(answers))
