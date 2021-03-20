def solution(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0 and (yellow // i + i) * 2 + 4 == brown:
            return [yellow // i + 2, i + 2]

if __name__ == '__main__':
    print(solution(24, 24))