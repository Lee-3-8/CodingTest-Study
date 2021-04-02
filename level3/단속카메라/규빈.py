def solution(routes):
    answer = 0
    routes.sort(key= lambda x : x[1])
    minE = routes[0][1]

    i = 0
    while i < len(routes):

        for j in range(i+1,len(routes)):
            if routes[j][0] > minE:
                temp = routes[j][1]
                break

        answer += 1

        if i == len(routes)-1:
            break
        
        i = j

        while j < len(routes):
            if routes[j][0] <= minE:
                routes.pop(j)
                j -= 1
            j += 1

        minE = temp

    return answer