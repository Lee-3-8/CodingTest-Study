def solution(n, words):
    answer = [0,0]
    bufferedWord = words[0]
    for i in range(1,len(words)):
        currentWord = words[i]
        answer[0] = i%n + 1
        answer[1] = i//n + 1
        if currentWord[0] != bufferedWord[-1]:
            return answer
        else :
            for j in range(i):
                if words[j] == currentWord:
                    return answer
        bufferedWord = currentWord

    return [0,0]