def solution(phone_book):
    arr_len =len(phone_book)
    phone_book.sort(key = lambda x: len(x))
    for i in range(arr_len):
        for j in range(i+1,arr_len):
            if phone_book[i] == phone_book[j][0:len(phone_book[i])]:
                return False
    return True


print(solution(["97674223","119","1195524421"]))