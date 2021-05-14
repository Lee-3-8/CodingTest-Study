def solution(begin, target, words):
    result = dfs(begin,target,words)
    return result - 1 if result else result

def dfs(curWord, target, words):
    if curWord == target:
        return 1
    l = []
    for i in range(len(words)):
        n = 0
        for j in range(len(curWord)):
            if words[i][j] != curWord[j]:
                n += 1
        if n == 1:
            w = words.pop(i)
            a = dfs(w, target, words)
            if a:
                l.append(a+1)
            words.insert(i, w)
    return min(l) if l else 0