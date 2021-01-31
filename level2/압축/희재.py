from string import ascii_uppercase as au

def solution(msg):
    vocab = {word:idx for idx, word in enumerate(au, start=1)}
    answer, i = [], 0

    while i < len(msg):
        for j in range(len(msg), i, -1):
            if msg[i:j] in vocab:
                if j < len(msg):
                    vocab[msg[i:j+1]] = len(vocab) + 1
                answer.append(vocab[msg[i:j]])
                i = j - 1
                break
        i += 1
    return answer

if __name__ == '__main__':
    print(solution("KAKAO"))