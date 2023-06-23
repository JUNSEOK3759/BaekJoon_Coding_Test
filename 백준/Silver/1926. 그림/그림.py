import sys
import re
from collections import deque, Counter
import heapq as hq
import copy
import math
import itertools
import bisect
# sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(i, j):
    dq = deque()
    dq.append([i, j])
    cnt = 1
    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if -1 < nx < n and -1 < ny < m and a[nx][ny] == 1 and ch[nx][ny] == 0:
                ch[nx][ny] = 1
                cnt += 1
                dq.append([nx, ny])
    return cnt
n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0
res = 0
for i in range(n):
    for j in range(m):
        if a[i][j] ==1 and ch[i][j] == 0:
            ch[i][j] = 1
            res = max(res, bfs(i, j))
            cnt += 1
print(cnt)
print(res)