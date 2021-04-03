
def solution(routes):
    routes.sort(key = lambda x: x[1])
    point = float('-inf')
    result = 0
    for start,end in routes:
        print(start,end,point)
        if point < start:
            point = end
            result += 1

    return result

print(solution(	[[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))