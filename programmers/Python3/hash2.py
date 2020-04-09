def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    for i in range(0, len(phone_book)):
        for index in range(i+1, len(phone_book)):
            if phone_book[index].startswith(phone_book[i]) is True:
                return False
    return answer
