def solution(n, words):
    word_set = {words[0]}
    for idx, word in enumerate(words[1:], start=1):
        if words[idx-1][-1] != word[0] or word in word_set:
            return [idx % n + 1, idx // n + 1]
        else:
            word_set.add(word)
    return [0, 0]

if __name__ == '__main__':
    print(solution(
        2,["hello", "one", "even", "never", "now", "world", "draw"]
    ))