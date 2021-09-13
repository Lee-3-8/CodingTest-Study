

def solution(A,B):
    A.sort()
    B = sorted(B,reverse=True)
    cnt=0
    for i in range(len(A)):
        cnt+=A[i]*B[i]
    return cnt
    


A = [1,4,2]
B = [5,4,4]
print(solution(A,B))
