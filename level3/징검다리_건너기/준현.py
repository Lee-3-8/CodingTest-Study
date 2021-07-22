def solution(stones, k):
    answer = []
    i = 0
    max_stone, index = 0, 0
    prev_Max, prev_index = 0, 0
    while i < len(stones)-k+1:
        for j in range(i, i+k):
            if max_stone <= stones[j]:
                max_stone = stones[j]
                index = j
        if prev_Max == max_stone and prev_index == index:
            max_stone = 0
            i += 1
        else:
            answer.append(max_stone)
            i = index
        prev_Max = max_stone
        max_stone = 0
        prev_index = index
    return min(answer)


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))


# def solution(stones, k):
#     answer = []
#     for i in range(len(stones)-k+1):
#         answer.append(max(stones[i:i+k]))
#     return min(answer)
