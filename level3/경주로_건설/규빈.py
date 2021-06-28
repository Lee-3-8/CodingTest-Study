def solution(board):
    l = len(board)
    check = [[0 for i in range(l)] for j in range(l)]
    cost = -500
    d = ((1,0), (0,1), (-1,0), (0,-1)) #xy 우,하,좌,상
    x, y = 0, 0

    def navigation(prevDir):
        nonlocal l, x, y, cost, board
        curved = 0
        check[y][x] = cost
        
        for i in range(4):
            if y+d[i][1] >= 0 and y+d[i][1] < l and x+d[i][0] >= 0 and x+d[i][0] < l:
                if not board[y+d[i][1]][x+d[i][0]]:
                    if i != prevDir:
                        curved = 500
                    else:
                        curved = 0
                    if not check[y+d[i][1]][x+d[i][0]] or check[y+d[i][1]][x+d[i][0]] >= cost + curved + 100:
                        x += d[i][0]
                        y += d[i][1]
                        cost += (100 + curved)
                        navigation(i)
                        cost -= (100 + curved)
                        x -= d[i][0]
                        y -= d[i][1]

    navigation(4)

    return check[l-1][l-1]