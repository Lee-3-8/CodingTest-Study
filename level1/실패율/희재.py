from collections import Counter

def solution(N, stages):
    user_num = len(stages)
    stages = Counter(stages)
    rank = []
    
    for i in range(1, N+1):
        if user_num:
            rank.append((i, stages[i] / user_num))
            user_num -= stages[i]
        else:
            rank.append((i, 0))
    
    answer = sorted(rank, key=lambda x: x[1], reverse=True)
    return [i[0] for i in answer]


if __name__ == '__main__':
    result =solution(
        5,
        [2, 1, 2, 1, 2, 4, 3, 3]
    )
    print(result)