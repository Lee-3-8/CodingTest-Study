from collections import defaultdict, deque

def solution(n, edge):
    node = defaultdict(list)
    dist = [0]*n
    for s,e in edge:
        node[s].append(e)
    def bfs(n):
        que = deque([1])
        cnt = 0
        while que:
            cnt += 1
            for i in node[que.popleft()]:
                if i not in que:
                    que.append(i)
            if n in que: return cnt
    result = []
    for i in range(2,n):
        result.append(bfs(i))
    
    return result

if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
