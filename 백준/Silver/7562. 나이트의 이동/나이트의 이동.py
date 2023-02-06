import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

def bfs(x1, y1, x2, y2):
    global res
    dq = deque()
    dq.append([x1, y1])

    while dq:
        x, y = dq.popleft()
        if x == x2 and y == y2:
            res = a[x][y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx > -1 and ny > -1 and nx < l and ny < l:
                if a[nx][ny] == 0:
                    a[nx][ny] = a[x][y] + 1
                    dq.append([nx, ny])


dx = [-1, -2, -2, -1, 1, 2, 1, 2]
dy = [-2, -1, 1, 2, -2, -1, 2, 1]
n = int(input())

for i in range(n):
    l = int(input())
    a = [[0 for _ in range(l)] for _ in range(l)]
    
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print(0)
    else:
        res = 0
        bfs(x1, y1, x2, y2)
        print(res)