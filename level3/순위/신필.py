from collections import defaultdict, deque

def solution(n, results):
    player = defaultdict(lambda :{'in':[],'out':[]})
    for start, end in results:
        player[start]['out'].append(end) # a -> b면  a가 b를 이김
        player[end]['in'].append(start)

    def bfs(node, direction):
        que = deque([node])
        check = set()
        while que:
            for i in player[que.popleft()][direction]:
                if i not in que:
                    que.append(i)
                    check.add(i)
        print(node, check, len(check))
        return len(check)

    result = 0
    for i in range(1,n+1):
        if bfs(i, 'in') + bfs(i,'out') == n-1:
            result += 1
    return result

if __name__ == '__main__':
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))