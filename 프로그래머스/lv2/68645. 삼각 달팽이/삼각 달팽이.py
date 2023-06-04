def solution(n):
    res = [[0 for _ in range(n)] for _ in range(n)]    
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            res[x][y] = num
            num += 1
    tot = []
    for i in res:
        for j in i:
            if j != 0:
                tot.append(j)
    return tot