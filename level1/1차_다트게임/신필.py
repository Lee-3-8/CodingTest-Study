from functools import reduce
result = []
cnt = -1

def culc_star(v) :
    global result
    result[cnt] *= 2
    if(cnt != 0):
        result[cnt-1] *= 2
    return True

def culc_sh(v):

    global result
    result[cnt] = result[cnt] * (-1)

    return True

def culc_mult(v):
    num_map = {
        'S' : 1,
        'D' : 2,
        'T' : 3
    }
    n = num_map[v]
    global result
    result[cnt] = result[cnt]**n
    return True

def solution(dartResult):
    global result
    global cnt
    cul_map = {
        '*' : culc_star,
        '#' : culc_sh,
        'S': culc_mult,
        'D' : culc_mult,
        'T' : culc_mult
    }
    for i, v in enumerate(dartResult):
        if(not cul_map.get(v)):
            if (i != 0 and v == '0' and dartResult[i-1] =='1'):
                result[cnt] = 10
            else:
                result.append(int(v))
                cnt += 1
        else:
            cul_map.get(v)(v)
        print(i,v,result,cnt)

    answer = reduce(lambda x,y : x+y,result )
    return answer

solution('1D2S#10S')