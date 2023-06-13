def solution(n):
    answer = []
    res = [[0 for _ in range(n)] for _ in range(n)]
    x, y = -1, 0
    num = 1
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            res[x][y] = num
            num += 1

    return [j for i in res for j in i if j != 0]