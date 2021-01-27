from collections import Counter

def refine(s):
    result = []
    for i in range(len(s) - 1):
        bigram = s[i:i+2].lower()
        if bigram.isalpha():
            result.append(bigram)
    return result

def solution(str1, str2):
    counter1, counter2 = Counter(refine(str1)), Counter(refine(str2))
    set1, set2 = set([i for i in counter1]), set([i for i in counter2])
    a_point = sum([min(counter1[idx], counter2[idx]) for idx in set1 & set2])
    b_point = sum([max(counter1[idx], counter2[idx]) for idx in set1 | set2])
    if a_point == b_point:
        return 65536
    else:
        return int(a_point / b_point * 65536)


if __name__ == '__main__':
    #print(solution("FRANCE", "french"))
    print(solution("E=M*C^2", "e=m*c^2"))