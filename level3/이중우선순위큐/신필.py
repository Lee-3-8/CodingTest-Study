# from collections import deque 

# def solution(operations):
#     deq = deque()

#     for i in operations:
#         if i[0] == 'I':
#             deq.append(int(i[2:]))
#             print(f'append {i[2:]}')
#         else :
#             if (deq and i[2] == '1'):
#                 deq.remove(max(deq))
#                 print(f'min {i[2]}')

#             elif(deq):
#                 deq.remove(min(deq))
#                 print(f'max {i[2]}')

#         print(deq)

#     return [max(deq),min(deq)] if deq else [0,0]

import heapq

def solution(operations):
    deq = deque()

    for i in operations:
        if i[0] == 'I':
            deq.append(int(i[2:]))
            print(f'append {i[2:]}')
        else :
            if (deq and i[2] == '1'):
                deq.remove(max(deq))
                print(f'min {i[2]}')

            elif(deq):
                deq.remove(min(deq))
                print(f'max {i[2]}')

        print(deq)

    return [max(deq),min(deq)] if deq else [0,0]

print(solution(		["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))