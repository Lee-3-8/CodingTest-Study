def solution(N, number):
    result = [{0}]
    for i in range(1,9):
        r = {int(str(N)*i)}
        for j in range(1,i//2+1):
            for x in result[j]:
                for y in result[i-j]:
                    r.add(x+y)
                    r.add(max(x,y)-min(x,y))
                    r.add(x*y)
                    if x != 0 and y != 0:
                        r.add(x//y)
                        r.add(y//x)
        if number in r:
            return i
        result.append(r)
    return -1