import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    if x == m-1 and y == n-1:
        # print('end')
        return 1
    
    if ch[x][y] == -1:
        ch[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx > -1 and ny > -1 and nx < m and ny < n:
                if a[nx][ny] < a[x][y]:
                    # print('nx, ny : ', nx, ny)
                    ch[x][y] += dfs(nx, ny)
    # else:
        # print('else ch[x][y] : ', ch[x][y])
    # print(f'ch[{x}][{y}] : ', ch[x][y])
    # print()
    # for i in ch:
    #     print(i)
    return ch[x][y]
    

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
m, n = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(m)]

ch = [[-1 for _ in range(n)] for _ in range(m)]

print(dfs(0, 0))