import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    a[x][y] = 0
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx > -1 and ny > -1 and nx < n and ny < n and a[nx][ny] == 1:
            dfs(nx, ny)

n = int(input())
a = [list(map(int, input())) for _ in range(n)]

res = []
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == 1:
            cnt = 0
            dfs(i, j)
            res.append(cnt)
print(len(res))
res.sort()
for i in res:
    print(i)