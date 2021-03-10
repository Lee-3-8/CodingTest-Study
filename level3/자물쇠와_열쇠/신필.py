def calc_abs(x,y):
    return (abs(x[0] - y[0]),abs(x[1] - y[1]))

def get_location(hom,arr):
    result = []
    for i,v1 in enumerate(arr):
        for j,v2 in enumerate(v1):
            if v2 == hom:
                result.append((i,j))
    print(result)
    return result

def get_abs_chain(arr):
    result = set()
    for i in range(len(arr)-1):
        result.add(calc_abs(arr[i],arr[i+1]))
    print(result)
    return result

def match_chain(key,lock):
    lotation_key = set()
    for i in key:
        lotation_key.add((i[1],i[0]))
    print(lotation_key)
    key.update(lotation_key)
    print(f'lock :{lock} key :{key}')
    return lock.issubset(key) if lock else False

def solution(key, lock):
    key_location = get_location(1,key)
    lock_location = get_location(0,lock)

    key_abs = get_abs_chain(key_location)
    lock_abs = get_abs_chain(lock_location)
    
    result = match_chain(key_abs,lock_abs)
    return result

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[0, 0, 0], [1, 1, 1], [1, 1, 1]]))

def test():
    a = (2,3)
    b = (1,2)
    print(abs(a[0]-b[0]))
# test()