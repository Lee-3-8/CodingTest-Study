from collections import defaultdict

RM = lambda word, idx: "".join(
    [word[i] if i != idx else "" 
     for i in range(len(word))]
)

def make_graph(words):
    graph = defaultdict(lambda: {'conn':[], 'visit': False})
    for idx in range(len(words)):
        word1 = words[idx]
        for jdx in range(idx, len(words)):
            word2 = words[jdx]
            if word1 != word2:
                for i in range(len(word1)):
                    if RM(word1, i) == RM(word2, i):
                        graph[word1]['conn'].append(word2)
                        graph[word2]['conn'].append(word1)
                        break
    return graph

def solution(begin, target, words):
    answer, graph = float("inf"), make_graph(words + [begin])

    def dfs(cur, level):
        nonlocal answer
        if cur == target:
            answer = level if answer > level else answer
        else:
            graph[cur]['visit'] = True
            for next_cur in graph[cur]['conn']:
                if not graph[next_cur]['visit']:
                    dfs(next_cur, level + 1)

    dfs(begin, 0)
    return 0 if answer == float('inf') else answer 

if __name__ == '__main__':
    print(solution(
        "hit", "cog", 
        ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(solution(
        "hit", "cog", 
        ["hot", "dot", "dog", "lot", "log"]))