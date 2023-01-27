import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")

def dfs(l):
    global res
    for i in range(2, n+1):
        if ch[i] == 0 and a[l][i] == 1:
            ch[i] = 1
            res.append(i)
            dfs(i)
            
            
n = int(input())
m = int(input())
a = [[0 for _ in range(n+1)] for _ in range(n+1)]
ch = [0 for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    a[x][y] = 1
    a[y][x] = 1
res = []
dfs(1)
print(len(res))