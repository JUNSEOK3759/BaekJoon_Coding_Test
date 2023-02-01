import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")
# input = sys.stdin.readline

def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    
    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx > -1 and ny > -1 and nx < len(a) and ny < len(a[0]):
                if a[nx][ny] == 1:
                    a[nx][ny] = a[x][y] + 1
                    dq.append([nx, ny])
            
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())

a = [list(map(int, input())) for _ in range(n)]
bfs(0, 0)

print(a[-1][-1])
