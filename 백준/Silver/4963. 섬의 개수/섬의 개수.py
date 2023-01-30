import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")

def bfs(x, y):
    dq = deque()
    dq.append([x, y])

    while dq:
        x, y = dq.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > -1 and ny > -1 and nx < len(a) and ny < len(a[0]):
                if a[nx][ny] == 1:
                    a[nx][ny] = 0
                    dq.append([nx, ny])
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    a = [list(map(int, input(). split())) for _ in range(y)]
    cnt = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 1:
                a[i][j] = 0
                bfs(i, j)
                cnt += 1
    print(cnt)