def offset(ch):
    return min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)

def solution(name):
    answer = sum([offset(i) for i in name])
    move_min = len(name) - 1
    for i in range(len(name)):
        idx = i
        while idx < len(name) and name[idx] == 'A':
            idx += 1
        if i < idx:
            move_min = min(move_min, (i-1) * 2 + len(name) - idx)
    return answer + move_min

if __name__ == '__main__':
    print(solution("JEROEN"))