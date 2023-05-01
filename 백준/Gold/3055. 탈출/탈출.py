from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while dq:
        x, y, d = dq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if -1 < nx < n and -1 < ny < m:
                if a[nx][ny] == '.': 
                    if a[x][y] == '*':
                        a[nx][ny] = '*'
                        dq.append([nx, ny, d+1])
                    elif a[x][y] == 'S':
                        a[nx][ny] = 'S'
                        dq.append([nx, ny, d+1])
                elif a[x][y] == 'S' and a[nx][ny] == 'D':
                    return d+1
    return 'KAKTUS'

n, m = map(int, input().split())
a = [list(map(str, input().rstrip())) for _ in range(n)]
dq = deque()

for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            dq.appendleft([i, j, 0])
        elif a[i][j] == 'S':
            dq.append([i, j, 0])

print(bfs())
