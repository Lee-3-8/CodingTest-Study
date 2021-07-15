
def solution(n, k, cmd):
    result = ["O"]*n
    cursor = [k,0] # 0: 진짜 커서 위치 , 1: 모아둔 이동 수
    cache = []

    def down(c): cursor[1] += int(c[1])
    def up(c): cursor[1] -= int(c[1])
    def undo(_): result[cache.pop()] = 'O'
    def cut(_):
        acc = 1 if cursor[1] > 0 else -1
        while cursor[1]:
            cursor[0] += acc
            if result[cursor[0]] == 'O':
                cursor[1] -= acc
        result[cursor[0]] = 'X'
        cache.append(cursor[0])

        while result[cursor[0]] == 'X': # 마지막인지 탐색
            if cursor[0]+1 > n-1:
                cursor[0] = cache[-1]
                cursor[1] = -1 # 마지막이었으면 위로 올라가야하니 위로 한칸 누적 (아예 빈경우는 없으니 나중에 계산가능)
                break
            cursor[0] += 1

    cmd_map = {
        'D': down,
        'U': up,
        'C': cut,
        'Z': undo
    }

    for i in cmd:
        c = i.split()
        cmd_map[c[0]](c)
        
    return ''.join(result)

if __name__ == '__main__':
    # print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
    # print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
    print(solution(8, 0, ["D 6", "C", "C", "C", "C"]))
