from collections import deque


n = 5000


def solution(n):
    count = 0
    while n != 0:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            count += 1
    return count


def solution1(n):
    visited = [False]*(n+1)
    queue = deque()
    queue.append((0, 0))
    visited[0] = True
    while queue:
        x, y = queue.popleft()
        if x == n:
            return y
        if x*2 <= n and visited[x*2] == False:
            visited[x*2] = True
            queue.append((x*2, y))
        if x+1 <= n and visited[x+1] == False:
            visited[x+1] = True
            queue.append((x+1, y+1))


print(solution(n))
