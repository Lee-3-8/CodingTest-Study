from collections import deque

def solution(numbers, target):
    answer, q = 0, deque([(0, 0)])
    while q:
        point, cur = q.popleft()
        if cur == len(numbers) and point == target:
            answer += 1
        elif cur < len(numbers):
            q.append((point + numbers[cur - 1], cur + 1))
            q.append((point - numbers[cur - 1], cur + 1))
    return answer

if __name__ == '__main__':
    print(solution([1,1,1,1,1], 3))