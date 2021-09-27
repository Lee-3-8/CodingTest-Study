DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def next_dir(flag, dir_num):
    if flag == 'S':
        return dir_num
    elif flag == 'L':
        return 3 if dir_num == 0 else dir_num - 1
    else:
        return (dir_num + 1) % 4

def solution(grid):
    h, w = len(grid), len(grid[0])
    visited, answer = set(), []
    for i in range(h):
        for j in range(w):
            for k in range(4):
                cnt = 0
                while (i, j, k) not in visited:
                    visited.add((i, j, k))
                    cnt += 1
                    ni, nj = i + DIR[k][0], j + DIR[k][1]
                    if ni <= -1: ni = h - 1
                    elif ni >= h: ni = 0
                    if nj <= -1: nj = w - 1
                    elif nj >= w: nj = 0
                    nk = next_dir(grid[ni][nj], k)
                    i, j, k = ni, nj, nk

                if cnt:
                    answer.append(cnt)

    return sorted(answer)

if __name__ == '__main__':
    print(solution(["S"]))
    print(solution(["SL","LR"]))