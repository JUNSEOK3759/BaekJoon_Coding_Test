# import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")

def dfs(l):
    ch[l] = 1
    print(l, end = ' ')
    for i in range(1, n+1):
        if ch[i] == 0 and a[l][i] == 1:
            dfs(i)
def bfs(l):
    dq = deque()
    dq.append(l)
    ch_bfs[l] = 1
    while dq:
        x = dq.popleft()
        print(x, end = ' ')
        for i in range(1, n+1):
            if ch_bfs[i] == 0 and a[x][i] == 1:
                ch_bfs[i] = 1
                dq.append(i)
n, m, v = map(int, input().split())

a = [[0 for _ in range(n+1)] for _ in range(n+1)]
ch = [0 for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    a[x][y] = 1
    a[y][x] = 1

dfs(v)
print()
ch_bfs = [0 for _ in range(n+1)]
bfs(v)