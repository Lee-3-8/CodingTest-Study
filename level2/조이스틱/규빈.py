def where(idx, arr, name):
    left, right = -1, 1
    l = len(name)
    while -left < len(name) and name[idx + left] == arr[idx + left]:
        left -= 1
    while right < len(name) and name[(idx + right)%l] == arr[(idx + right)%l]:
        right += 1
    
    return left if -left < right else right

def solution(name):
    arr = list("A"*len(name))
    move, idx, cnt = 0, 0, 0
    for i in range(1, len(name[1:])):
        if arr[i] == i:
            cnt += 1
    while cnt < len(name):
        move += min(ord(name[idx])-ord(arr[idx]), ord('Z')-ord(name[idx])+1)
        arr[idx] = name[idx]
        cnt += 1
        mcnt = where(idx, arr, name)
        idx = (idx + mcnt) % len(name)
        move += abs(mcnt) % len(name)

    return move