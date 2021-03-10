# 2레벨     코딩테스트 고득점 Kit       주식가격


def solution(prices):
    def pop(time, price):
        while stack and stack[-1][0] > price:
            pop = stack.pop()
            _id[pop[1]] = time - pop[1]

    stack = []
    _id = [-1] * len(prices)
    for time, price in enumerate(prices):
        pop(time, price)
        stack.append((price, time))

    pop(time, 0)

    return _id


if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))