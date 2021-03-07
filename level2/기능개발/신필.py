from collections import deque 

def solution(progresses, speeds):
    deq = deque(progresses)
    spe = deque(speeds)
    result = []
    while len(deq):
        for i in range(len(deq)):
            deq[i] += spe[i]
        print(deq,spe,result)
        del_cnt = 0
        while deq[0] >= 100:
            deq.popleft()
            spe.popleft()
            del_cnt += 1
            if len(deq) == 0 : break
        if del_cnt != 0: result.append(del_cnt)

    return result

print(solution( 	[93, 30, 55], [1, 30, 5] ))