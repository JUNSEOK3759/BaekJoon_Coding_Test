import sys
from collections import deque
n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
mini = min(map(min, a))
maxi = max(map(max, a))
res = 0
dq = deque()
for h in range(mini-1, maxi):
    ch = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] > h and ch[i][j] == 0:
                ch[i][j] = 1
                cnt += 1
                dq.append([i, j])
                while dq:
                    x, y = dq.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx > -1 and ny > -1 and nx < n and ny < n and a[nx][ny] > h and ch[nx][ny] == 0:
                            ch[nx][ny] = 1
                            dq.append([nx, ny])
    res = max(res, cnt)
print(res)