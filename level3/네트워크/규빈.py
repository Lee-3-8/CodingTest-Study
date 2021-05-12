def solution(n, computers):
    nws = []
    for i in range(n):
        dfs(computers, n, i, nws)
    return len(nws)

def dfs(computers, n, i, nws):
    flag = True
    for nw in nws:
        if i in nw:
            net = nw
            flag = False
            break
    if flag:
        net = {i}
        nws.append(net)

    for j in range(n):
        if j != i and computers[i][j]:
            if j not in net:
                net.add(j)
                dfs(computers, n, j, nws)