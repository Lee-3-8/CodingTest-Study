def solution(dirs):
    answer = 0
    current = (0, 0)
    visited = set()
    # 도착지점 기준으로 URDL 1,2,3,4
    for i in dirs:
        y, x = current
        if i == 'U':
            if y >= 5:
                pass
            else:
                if (y+1, x, 1) not in visited and (y, x, 3) not in visited:
                    visited.add((y+1, x, 1))
                    visited.add((y, x, 3))
                    answer += 1
                current = (y+1, x)
        elif i == 'D':
            if y <= -5:
                pass
            else:
                if (y-1, x, 3) not in visited and (y, x, 1) not in visited:
                    visited.add((y-1, x, 3))
                    visited.add((y, x, 1))
                    answer += 1
                current = (y-1, x)
        elif i == 'L':
            if x <= -5:
                pass
            else:
                if (y, x-1, 4) not in visited and (y, x, 2) not in visited:
                    visited.add((y, x-1, 4))
                    visited.add((y, x, 2))
                    answer += 1
                current = (y, x-1)
        else:
            if x >= 5:
                pass
            else:
                if (y, x+1, 2) not in visited and (y, x, 4) not in visited:
                    visited.add((y, x+1, 2))
                    visited.add((y, x, 4))
                    answer += 1
                current = (y, x+1)

    return answer


dirs = "UDU"
print(solution(dirs))
