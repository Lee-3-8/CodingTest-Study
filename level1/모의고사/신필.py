# u1 은 12345 u2는 21232425 u3 3311224455

def solution(answers):
    u1,u2,u3 = 0,0,0
    u2_ele = [1,3,4,5]
    u2_flag = 0
    u3_ele = [3,1,2,4,5]
    u3_flag = 0

    for i,v in enumerate(answers):
        print(u1,u2,u3, i,v)
        if v == (i % 5) + 1 :
            u1 += 1
        if v == u3_ele[u3_flag]:
            u3 += 1

        if i % 2 == 1:
            if v == u2_ele[u2_flag]:
                u2 += 1
            u2_flag = (u2_flag + 1) % 4
            u3_flag = (u3_flag + 1) % 5
        else:
            if v == 2:
                u2 += 1
    result = []

    if max(u1,u2,u3) == u1:
        result.append(1)
    if max(u1,u2,u3) == u2:
        result.append(2)
    if max(u1,u2,u3) == u3:
        result.append(3)
        
    return result

print(solution([1, 3, 2, 4, 2]))