
def up(x,y,visited,cnt):
    y += 1
    if (-5 <= x <= 5 and -5 <= y <= 5):
        if (x,y-1,x,y) not in visited:
            visited.add((x,y-1,x,y))
            visited.add((x,y,x,y-1))
            cnt+=1
    else: y -= 1
    return x,y,cnt

def left(x,y,visited,cnt):
    x -= 1
    if (-5 <= x <= 5 and -5 <= y <= 5):
        if (x+1,y,x,y) not in visited:
            visited.add((x+1,y,x,y))
            visited.add((x,y,x+1,y))
            cnt+=1
    else: x += 1
    return x,y,cnt

def down(x,y,visited,cnt):
    y -= 1
    if (-5 <= x <= 5 and -5 <= y <= 5):
        if (x,y+1,x,y) not in visited:
            visited.add((x,y+1,x,y))
            visited.add((x,y,x,y+1))
            cnt+=1
    else: y += 1
    return x,y,cnt

def right(x,y,visited,cnt):
    x += 1
    if (-5 <= x <= 5 and -5 <= y <= 5):
        if (x-1,y,x,y) not in visited:
            visited.add((x-1,y,x,y))
            visited.add((x,y,x-1,y))
            cnt+=1
    else: x -= 1
    return x,y,cnt

def solution(dirs):
    visited = set()
    go_map = {
        'U':up,
        'L':left,
        'D':down,
        'R':right
    }
    x,y,cnt = 0,0,0
    for i in dirs:
        x,y,cnt = go_map[i](x,y,visited,cnt)
    return cnt


if __name__ == '__main__':
    print(solution("ULURRDLLU"))