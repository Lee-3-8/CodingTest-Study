from collections import defaultdict
from copy import deepcopy


def trans(target):
    dic = defaultdict(lambda: [])
    for i in target:
        dic[i[0]].append(i[1])
    for i in dic.keys():
        dic[i].sort()
    print(dic)
    return dic


def recur(st, answer, le, dic, an):
    if le == len(answer):
        an.append(answer)
    else:
        if len(dic[st]) == 1:
            answer.append(dic[st][0])
            temp = dic[st][0]
            dic[st].remove(dic[st][0])
            recur(temp, answer, le, dic, an)
        else:
            for i in dic[st]:
                tanswer = deepcopy(answer)
                tdic = deepcopy(dic)
                tanswer.append(i)
                tdic[st].remove(i)
                recur(i, tanswer, le, tdic, an)


def solution(tickets):
    dic = trans(tickets)
    an = []
    recur("ICN", ["ICN"], len(tickets)+1, dic, an)
    return an[0]


tickets = [["ICN", "SFO"], ["ICN", "ATL"], [
    "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(tickets))
