# from heapq import heappop, heappush
# def solution(operations):
#     heap = []
#     for string in operations:
#         op, num = string.split()
#         if op == 'I':
#             heappush(heap, int(num))
#         elif op == 'D' and heap:
#             if num == '1':
#                 heap = [heappop(heap) for i in range(len(heap))]
#                 heap.pop()
#             else:
#                 heappop(heap)
#     if not heap:
#         return [0,0]
#     else:
#         heap = [heappop(heap) for i in range(len(heap))]
#         return [heap[-1], heap[0]]

from heapq import heappop, heappush
def solution(operations):
    heap = []
    for string in operations:
        op, num = string.split()
        temp = []
        if op == 'I':
            heappush(heap, int(num))
        elif op == 'D' and heap:
            if num == '1':
                for _ in range(len(heap)):
                    heappush(temp, -heappop(heap))
                heappop(temp)
                for _ in range(len(temp)):
                    heappush(heap, -heappop(temp))
            else:
                heappop(heap)
    if not heap:
        return [0,0]
    else:
        minh = heap[0]
        temp = []
        for _ in range(len(heap)):
            heappush(temp, -heappop(heap))
        return [-temp[0], minh]