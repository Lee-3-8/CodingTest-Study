# 3레벨     코딩테스트 고득점 Kit     여행경로
from copy import deepcopy


def solution(tickets):
    tickets.sort(key=lambda x: (x[0]))

    result = []

    def dfs(road, ticket):
        if len(road) == len(tickets) + 1:
            result.append(deepcopy(road))
            return

        for idx in range(len(ticket)):
            if road[-1] == ticket[idx][0]:
                temp = ticket[idx]
                road.append(ticket[idx][1])
                del ticket[idx]
                dfs(road, ticket)
                road.pop()
                ticket.insert(idx, temp)

    dfs(["ICN"], deepcopy(tickets))
    result.sort(key=lambda x: x)
    return result[0]


if __name__ == "__main__":
    # print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    # print(
    #     solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
    # )

