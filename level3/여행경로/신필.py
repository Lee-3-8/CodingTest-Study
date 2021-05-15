
def dfs(end,dic,cnt):
    if dic[end] == []: return []
    if cnt == len(dic): return [dic[end][0]]
    for i in dic[end]:
        temp = dic[end].remove(i)
        dic[end] = temp
        result = dfs(i, dic, cnt+1)
        if result != []:
            return [i] + result
    return []
def solution(tickets):
    dic = {}
    for i in tickets:
        dic[i[0]] = dic.get(i[0],[])+[i[1]]
        dic[i[0]].sort()

    result = ['ICN'] + dfs('ICN',dic,1)
    # answer = []
    return result

if __name__ == '__main__':
    # print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    print(solution(	[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))