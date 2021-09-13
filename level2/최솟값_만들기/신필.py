def solution(A,B):
    A.sort(reverse = True)
    B.sort()
    return sum([a * b for a, b in zip(A,B)])

if __name__ == '__main__':
    print([1, 4, 2], [5, 4, 4])