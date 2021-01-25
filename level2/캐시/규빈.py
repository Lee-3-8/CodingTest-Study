def solution(cacheSize, cities):
    processTime = 0
    arr = [0 for _ in range(cacheSize)]
    for i in cities:
        low = i.lower()
        if low in arr: # hit : 중복
            arr.remove(low)
            arr.append(low)
            processTime += 1
        else: # miss : 중복 x 
            if arr: # 캐시 크기 0 제외
                arr.pop(0)
                arr.append(low)
            processTime += 5

    return processTime