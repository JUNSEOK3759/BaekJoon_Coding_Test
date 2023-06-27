def solution(book):
    answer = 0
    for i in range(len(book)):
        a, b = book[i][0], book[i][1]
        x, y = a.split(':')
        z, w = b.split(':')
        book[i][0] = int(x) * 60 + int(y)
        book[i][1] = int(z) * 60 + int(w) + 10
    a = {}
    
    book.sort()
    a[0] = book[0]

    for i in range(1, len(book)):
        for x, y in a.items():
            if book[i][0] >= y[1]:
                a[x] = book[i]
                break
        else:
            a[i] = book[i]    
    return len(a)