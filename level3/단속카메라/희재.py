def solution(routes):
    routes.sort(key=lambda x: x[1])
    answer, right_min = 0, float('-inf')
    for src, dst in routes:
        if right_min < src:
            answer += 1
            right_min = dst
    return answer

if __name__ == '__main__':
    print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))