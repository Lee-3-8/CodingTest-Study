from itertools import combinations

relation = [["a", 1, 4], [2, 1, 5], ["a", 2, 4]]


def minimal(current_arr, min_arr):
    counter = 0
    if not min_arr:
        return 1
    else:
        for i in min_arr:
            temp = len(set(current_arr[0]) & set(i[0]))
            for j in range(len(current_arr)):
                if len(set(current_arr[j]) & set(i[j])) == temp:
                    counter += 1
            if counter == len(min_arr[0]) and temp == list(map(len, i))[0]:
                return 0
            else:
                counter = 0
    return 1


def unique(current_arr):
    if len(set(current_arr)) == len(current_arr):
        return 1
    else:
        return 0


def solution(relation):
    answer = 0
    column = len(relation[0])
    count_arr = []
    for i in range(1, column+1):
        com_arr = []
        for j in range(len(relation)):
            temp = list(combinations(relation[j], i))
            com_arr.append(temp)
        com_arr = list(map(list, zip(*com_arr)))
        for i in com_arr:
            if unique(i) and minimal(i, count_arr):
                count_arr.append(i)
                answer += 1

    return answer


print(solution(relation))
