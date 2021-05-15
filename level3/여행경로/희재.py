from collections import defaultdict

def make_graph(tickets):
	graph = defaultdict(list)
	for s, t in tickets:
		graph[s].append(t)
	for name in graph:
		graph[name].sort(reverse=True)
	return graph

def solution(tickets):
	graph, answer = make_graph(tickets), []

	def dfs(cur):
		while graph[cur]:
			dfs(graph[cur].pop())
		else:
			nonlocal answer
			answer.append(cur)
	dfs('ICN')
	return answer[::-1]

	