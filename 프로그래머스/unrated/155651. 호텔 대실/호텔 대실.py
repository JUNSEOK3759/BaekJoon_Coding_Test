def solution(book_time):
    answer = 0
    book_time.sort(key = lambda x : (x[0], x[1]))
    rent = []
    
    for i in book_time:
        q = list()
        for j in i:
            x, y = j.split(":")
            q.append(int(x) * 60 + int(y))
        rent.append(q)
    x = []
    x.append(rent[0])
    
    for i in range(1, len(rent)):
        for j in range(len(x)):
            if rent[i][0] >= x[j][1] + 10:
                x[j] = rent[i]
                break
        else:
            x.append(rent[i])
    return len(x)