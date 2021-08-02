def solution(dirs):
    path = set()
    direction = {
        "U" : [0,1],
        "D" : [0,-1],
        "R" : [1,0],
        "L" : [-1,0]
    }

    x, y = 0, 0
    nx, ny = 0, 0

    for d in dirs:
        if not (-5 <= x+direction[d][0] <= 5 and -5 <= y+direction[d][1] <= 5):
            continue
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        path.add((x,y,nx,ny))
        path.add((nx,ny,x,y))
        x, y = nx, ny

    return len(path)//2