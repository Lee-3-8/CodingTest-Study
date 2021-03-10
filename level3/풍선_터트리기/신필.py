def solution(a):
    cnt = 0
    for i in range(1,len(a)-1):
        print(a[i])
        if a[i] < a[i-1] and a[i] < a[i+1]:
            cnt += 1
    return cnt+2

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
print(solution([9,-1,-5]))