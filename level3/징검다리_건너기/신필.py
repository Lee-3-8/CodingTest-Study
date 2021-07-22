def solution(stones, k):
    result = 0
    cnt = 0
    for i in stones:
        if result >= i:
            cnt+=1
        else:
            result = i
        if cnt == k:
            


if __name__ == '__main__':
    print(solution(	[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))