import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")

def bfs(x, y, h):
    dq = deque()
    dq.append([x, y])

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > -1 and ny > -1 and nx < n and ny < n:
                if ch[nx][ny] == 0 and board[nx][ny] > h:
                    ch[nx][ny] = 1
                    dq.append([nx, ny])

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = -2147483647

maxi = max(map(max, board))
mini = min(map(min, board))

for h in range(mini-1, maxi):
    ch = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > h and ch[i][j] == 0:
                cnt += 1
                ch[i][j] = 1
                bfs(i, j, h)
    if cnt > res:
        res = cnt
          
print(res)