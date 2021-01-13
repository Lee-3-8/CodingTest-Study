
def quard_tree(arr):
    print(arr)      
    if len(arr) == 2:
        c = arr[0] + arr[1]
        cnt = c.count(0)
        return [cnt,4-cnt]

    child = [ [] for _ in range(len(arr)) ]
    n = len(arr)
    for i,v in enumerate(arr):

        print(i,v)
        if i < n//2:
            child[0].append(v[: n//2])
            child[1].append(v[n//2 :])
        else:
            child[2].append(v[: n//2])
            child[3].append(v[ n//2 :])

    print(child)
    result = [0, 0]
    for i in child:
        c = quard_tree(i)
        c[0] = 1 if c[0] == 4 and c[1] == 0 else c[0] 
        c[1] = 1 if c[1] == 4 and c[0] == 0 else c[1]
        print( "합한값 :" , c)
        result[0] += c[0]
        result[1] += c[1]
        print( "result 합한값 :" , result)
    return result

def solution(arr):
    c = sum(arr,[])
    if len(set(c)) == 1:
        r = list(set(c))
        result = [1,0] if r[0] == 0 else [0,1]
        return result
    result = quard_tree(arr)
    return result

# print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
# print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
# print( solution([[0,0],[0,1]]))
# print( solution([[0,0],[0,0]]))
print( solution([[1,1],[1,1]]))