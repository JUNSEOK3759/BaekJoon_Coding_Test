def solution(n):
    answer = []
    a = [[0 for _ in range(n)] for _ in range(n)]
    x, y = -1, 0
    k = 1
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            a[x][y] = k
            k += 1
    return [j for i in a for j in i if j != 0]

