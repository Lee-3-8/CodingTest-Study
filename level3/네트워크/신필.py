from collections import deque

def bfs(start, flag, computers,n):
    que = deque([start])
    flag[start] = 0
    while que:
        cur = que.popleft()
        for i in range(n):
            if computers[cur][i] == 1 and flag[i] == 1:
                que.append(i)
                flag[i] = 0

def solution(n, computers):
    # 맨처음 노드를 큐에 집어넣는다.
    # 큐 맨앞에서 노드를 꺼낸다
    # 꺼낸 노드의 인접리스트중 큐에 존재하지 않는 노드는 큐에 넣는다
    # 큐에 들어간 노드들은 flag로 이미 네트워크에 존재한다는 것을 체크해준다
    # 큐가 빌때 까지 반복한다
    # 큐가 비는 반복마다 cnt를 1씩 높여준다.
    # 모든 노드의 flag가 0일때까지 반복한다.
    result = 0
    flag = [1] * n
    while sum(flag) != 0:
        for i in range(n):
            if flag[i] == 1:
                bfs(i,flag,computers,n)
                result += 1
    return result

if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))