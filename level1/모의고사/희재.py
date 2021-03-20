
def gen(pattern):
    idx = 0
    length = len(pattern)
    while True:
        yield pattern[idx % length]
        idx += 1


def solution(answers):
    generators = [
        gen([1, 2, 3, 4, 5]),
        gen([2, 1, 2, 3, 2, 4, 2, 5]),
        gen([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]),
    ]
    counts = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(generators[i]) == num:
                counts[i] += 1

    max_count = 0
    for i in range(3):
        if max_count < counts[i]:
            max_count = counts[i]

    return [i + 1 for i in range(3) if max_count == counts[i]]


if __name__ == '__main__':
    result = solution([1,3,2,4,2])
    print(result)