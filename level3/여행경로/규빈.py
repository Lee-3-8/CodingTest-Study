def solution(tickets):
    answer = ["ICN"]
    tickets.sort(key=lambda x : x[1])
    return dfs("ICN", tickets, answer)

def dfs(start, tickets, answer):
    if not tickets:
        return answer
    for i in range(len(tickets)):
        ticket = tickets[i]
        a = []
        if ticket[0] == start:
            answer.append(ticket[1])
            tickets.remove(tickets[i])
            a = dfs(ticket[1], tickets, answer)
            tickets.insert(i, ticket)
            if a:
                return a
            else:
                answer.pop()