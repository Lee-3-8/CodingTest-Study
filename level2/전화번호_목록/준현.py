phone_book = ["111113", "1112", "12"]


def solution(phone_book):
    ln = list(map(len, phone_book))
    ln.sort()
    phone_book.sort()

    book_len = len(phone_book)
    for i in range(book_len):
        for j in range(i+1, book_len):
            if phone_book[j][:ln[i]] == phone_book[i]:
                return False

    return True


print(solution(phone_book))
