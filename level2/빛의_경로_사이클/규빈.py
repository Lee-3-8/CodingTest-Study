def solution(grid):
    answer = []
    road = {
        "S": lambda y, x : (y, x),
        "L": lambda y, x : (-x, y),
        "R": lambda y, x : (x, -y),
    }
    arr = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for k in [(0,1), (1,0), (0,-1),(-1,0)]:
                cnt = 0
                x, y, z = j, i, k
                while (y,x,z) not in arr:
                    arr.add((y,x,z))
                    y, x = (y+z[0])%len(grid), (x+z[1])%len(grid[i])
                    z = road[grid[y][x]](*z)
                    cnt += 1
                if cnt:
                    answer.append(cnt)

    return sorted(answer)