
def solution(routes):
    # min_r = min(map(lambda x: x[0],routes))
    routes.sort(key = lambda x: x[0])
    point = routes[0][0]
    result = 0
    for start,end in routes:
        if point < start:
            point = end
            result += 1


    return result

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))