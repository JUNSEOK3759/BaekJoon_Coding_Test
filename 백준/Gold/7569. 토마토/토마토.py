import sys
from collections import deque
import heapq as hq
import copy
import math
# sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)


dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [-1, 1, 0, 0, 0, 0]

def bfs():
    while dq:
        x, y, z = dq.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if nx > -1 and ny > -1 and nz > -1 and nx < h and ny < n and nz < m:
                if a[nx][ny][nz] == 0:
                    a[nx][ny][nz] = a[x][y][z] + 1
                    dq.append([nx, ny, nz])

m, n, h = map(int, input().split())

a = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dq = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if a[i][j][k] == 1:
                dq.append([i, j, k])

bfs()

res = -2147483647
for i in range(h):
    for j in range(n):
        for k in range(m):
            if a[i][j][k] == 0:
                print(-1)
                sys.exit(0)
            else:
                res = max(res, a[i][j][k])

print(res -1)