# 2레벨     코딩테스트 고득점 Kit     전화번호목록


def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x))
    for i in range(len(phone_book) - 1):
        pre = len(phone_book[i])
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] == phone_book[j][0:pre]:
                return False

    return answer


phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))