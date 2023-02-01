import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs1():
    while dq:
        x, y, z = dq.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx > -1 and nx < len(a) and ny > -1 and nz > -1 and ny < len(a[0]) and nz < len(a[0][0]):
                if a[nx][ny][nz] == 0:
                    a[nx][ny][nz] = a[x][y][z] + 1
                    dq.append([nx, ny, nz])
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
m, n, h = map(int, input().split())
a = []
for i in range(h):
    a.append([list(map(int, input().split())) for _ in range(n)])
dq = deque()
for i in range(len(a)):
    for j in range(len(a[0])):
        for k in range(len(a[0][0])):
            if a[i][j][k] == 1:
                dq.append([i, j, k])

bfs1()
res = -2147483647
for i in range(len(a)):
    for j in range(len(a[0])):
        for k in range(len(a[0][0])):
            if a[i][j][k] == 0:
                print(-1)
                sys.exit(0)
            else:
                res = max(res, a[i][j][k])
print(res -1)