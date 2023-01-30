import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")

def bfs(x, y):
    global cnt
    dq = deque()
    dq.append([x, y])

    while dq:
        h, q = dq.popleft()
        for z in range(4):
            nx = h + dx[z]
            ny = q + dy[z]
            if nx > -1 and ny > -1 and nx < len(a) and ny < len(a[0]):
                if a[nx][ny] == 0:
                    a[nx][ny] = 1
                    dq.append([nx, ny])
        cnt += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m, k = map(int, input().split())
a = [[0 for _ in range(m)] for _ in range(n)]

for i in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            a[j][k] = 1
res = []

for i in range(len(a)):    
    for j in range(len(a[0])):
        if a[i][j] == 0:
            a[i][j] = 1
            cnt = 0
            bfs(i, j)
            res.append(cnt)

print(len(res))
res.sort()
for i in res:
    print(i, end = ' ')


