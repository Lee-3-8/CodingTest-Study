def solution(a, answer=2):
    center = a.index(min(a))
    left_min, right_min = a[0], a[-1]

    for idx in range(1, center):
        answer += left_min > a[idx]
        left_min = min(left_min, a[idx])
    for idx in range(len(a)-2, center, -1):
        answer += right_min > a[idx]
        right_min = min(right_min, a[idx])

    return answer if center in [0, len(a)-1] else answer + 1

if __name__ == '__main__':
    print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))