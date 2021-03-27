def solution(n, lost, reserve):
    dup = set(lost) & set(reserve)
    lost = sorted(set(lost) - dup)
    reserve = sorted(set(reserve) - dup)
    reserve = [[i-1, i, i+1] for i in reserve]

    r_idx, l_idx = 0, 0
    answer = n - len(lost)
    while r_idx < len(reserve) and l_idx < len(lost):
        if lost[l_idx] in reserve[r_idx]:
            r_idx += 1
            l_idx += 1
            answer += 1
        elif lost[l_idx] < reserve[r_idx][1]:
            l_idx += 1
        else:
            r_idx += 1

    return answer

if __name__ == '__main__':
    print(solution(3, [3], [1]))