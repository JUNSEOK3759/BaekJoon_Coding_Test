import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")

def bfs(x, y):
    dq = deque()
    a[x][y] = 0
    dq.append([x, y])
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx > -1 and ny > -1 and nx < len(a) and ny < len(a[0]) and a[nx][ny] == 1:
                a[nx][ny] = 0
                dq.append([nx, ny])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
t = int(input())

for i in range(t):
    n, m, k = map(int, input().split())
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        a[x][y] = 1
    cnt = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)