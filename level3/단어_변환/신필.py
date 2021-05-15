
def is_one_difference(begin,i):
    cnt = 0
    for j in range(len(begin)):
        if begin[j] != i[j]: cnt+=1
        if cnt > 2: return False
    return cnt == 1 

def dfs(begin, target, words, count, result):
    if begin == target:
        result[0] = min(result[0],count)
        return
    if count >= result[0]: return
    for i in words:
        if is_one_difference(begin,i):
            dfs(i, target, words, count+1, result)


def solution(begin, target, words):
    result = [50]
    words = { i:0 for i in words } # list -> dict
    if target in words:
        dfs(begin,target,words, 0,result)
    else:
        result[0] = 0
    return result[0]

if __name__ == '__main__':
    print(solution(	"hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
