import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")

def bfs(x, y, c, ch):
    dq = deque()
    dq.append([x, y])
    while dq:
        h, q = dq.popleft()
        for k in range(4):
            nx = h + dx[k]
            ny = q + dy[k]
            if nx > -1 and ny > -1 and nx < n and ny < n:
                if a[nx][ny] in c and ch[nx][ny] == 0:
                    dq.append([nx, ny])
                    ch[nx][ny] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
a = [list(map(str, input())) for _ in range(n)]

ch = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 'R' and ch[i][j] == 0:
            ch[i][j] = 1
            bfs(i, j, ['R'], ch)
            cnt += 1
        elif a[i][j] == 'G' and ch[i][j] == 0:
            ch[i][j] = 1
            bfs(i, j, ['G'], ch)
            cnt += 1
        elif a[i][j] == 'B' and ch[i][j] == 0:
            ch[i][j] = 1
            bfs(i, j, ['B'], ch)
            cnt += 1

ch_RG = [[0 for _ in range(n)] for _ in range(n)]
cnt_RG = 0
for i in range(n):
    for j in range(n):
        if a[i][j] in ['R', 'G'] and ch_RG[i][j] == 0:
            ch_RG[i][j] = 1
            bfs(i, j, ['R', 'G'], ch_RG)
            cnt_RG += 1
        elif a[i][j] == 'B' and ch_RG[i][j] == 0:
            ch_RG[i][j] = 1
            bfs(i, j, ['B'], ch_RG)
            cnt_RG += 1
            
print(cnt, cnt_RG)