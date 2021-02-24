from collections import Counter
from functools import reduce

def solution(clothes):
    counter = Counter([i[1] for i in clothes]).values()
    counter = map(lambda x: x+1, counter)
    return reduce(lambda x, y: x * y, counter) - 1


if __name__ == '__main__':
    print(solution(	[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))