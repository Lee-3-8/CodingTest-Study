# Summer/Winter Coding(~2018)   예산


def solution(d, budget):
    answer = 0
    d.sort()

    for money in d:
        if budget >= money:
            budget -= money
            answer += 1

        else:
            break
    return answer


"""
출력 확인
"""
# d = [2, 2, 3, 3]
# budget = 10

# print(solution(d, budget))