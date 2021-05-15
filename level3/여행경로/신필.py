
def dfs(start,dic,result):
    if start in dic:
        while dic[start]:
            dfs(dic[start].pop(),dic,result)
        result.append(start)
    else :
        result.append(start)

def solution(tickets):
    dic = {}
    for i in tickets:
        dic[i[0]] = dic.get(i[0],[])+[i[1]]
        dic[i[0]].sort(reverse=True)
    result = []
    dfs('ICN',dic,result)
    return result[::-1]

if __name__ == '__main__':
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    # print(solution(	[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))