

def solution(people, limit):
    people.sort()
    answer = 0
    i, j = 0, len(people)-1
    while i <= j:
        answer += 1
        temp = people[i]+people[j]
        if temp <= limit:
            i += 1
        j -= 1
    return answer


people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))
# def solution(people, limit):
#     answer = 0
#     N = len(people)
#     check = [False]*N
#     for i in range(N):
#         temp, max_hap = i, 0
#         if check[i]:
#             continue
#         for j in range(i+1, N):
#             if limit >= people[i]+people[j] > max_hap and not check[j]:
#                 temp = j
#                 max_hap = people[i]+people[j]
#         check[temp] = True
#         check[i] = True
#         answer += 1

#     return answer
