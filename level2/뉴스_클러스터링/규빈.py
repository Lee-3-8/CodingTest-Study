def solution(str1, str2):
    supStr1 = []
    supStr2 = []

    makeSupStr(str1.lower(), supStr1)
    makeSupStr(str2.lower(), supStr2)
    
    u = union(supStr1[:], supStr2[:])
    i = intersection(supStr1[:], supStr2[:])

    return int(len(i) / len(u) * 65536) if u else 65536

def makeSupStr(string, supStr): # 부분집합 구하기
    twoStr = zip(string, string[1:])
    for i in twoStr:
        if (i[0]+i[1]).isalpha():
            supStr.append(i[0]+i[1])

def union(list1, list2): # 합집합 구하기
    union = list1[:]
    for i in list2:
        if i in list1:
            list1.remove(i)
        else:
            union.append(i)
    return union

def intersection(list1, list2): # 교집합 구하기
    intersection = []
    for i in list1:
        if i in list2:
            intersection.append(i)
            list2.remove(i)
    return intersection