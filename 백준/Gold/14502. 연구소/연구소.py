import sys
import copy
from collections import deque
import itertools
# sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > -1 and ny > -1 and nx < n and ny < m:
                if ca[nx][ny] == 0:
                    ca[nx][ny] = 2
                    dq.append([nx, ny])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

zeroP = []
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            zeroP.append([i, j])
three_A = list(itertools.combinations(zeroP, 3))

res = -2147483647
for i in three_A:
    ca = copy.deepcopy(a)
    for j in i:
        ca[j[0]][j[1]] = 1
    for k in range(n):
        for l in range(m):
            if ca[k][l] == 2:
                bfs(k, l)
    
    cnt = 0
    for j in range(n):
        for k in range(m):
            if ca[j][k] == 0:
                cnt += 1
    res = max(res, cnt)
    
print(res)