from itertools import combinations


def solution(numbers, target):
    answer = 0
    hab = sum(numbers)
    for i in range(1, len(numbers)+1):
        com = list(map(list, combinations(numbers, i)))
        for j in com:
            if hab-2*sum(j) == target:
                answer += 1

    return answer
