import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def bfs():
    while dq:
        q, w = dq.popleft()
        for k in range(4):
            nx = q + dx[k]
            ny = w + dy[k]
            
            if nx > -1 and ny > -1 and nx < len_x and ny < len_y:
                if a[nx][ny] == 0:
                    a[nx][ny] = a[q][w] + 1
                    dq.append([nx, ny])    

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
m, n = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
len_x, len_y = len(a), len(a[0])
dq = deque()
for i in range(len_x):
    for j in range(len_y):
        if a[i][j] == 1:
            dq.append([i, j])
bfs()  
for i in range(len_x):
    for j in range(len_y):
        if a[i][j] == 0:
            print(-1)
            sys.exit(0)
print(max(map(max, a)) - 1)