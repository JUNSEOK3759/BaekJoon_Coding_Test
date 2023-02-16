import sys
from collections import deque
import heapq as hq
import copy
import math
import itertools
# sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)
# 가장 일찍 끝나는 회의를 먼저 하도록 정렬 해준다

def bfs(x, y, d):
    dq = deque()
    dq.append([x, y, d])
    ch = [[0 for _ in range(m)] for _ in range(n)]
    ch[x][y] = 1
    while dq:
        x, y, d = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >-1 and ny > -1 and nx < n and ny < m:
                if ch[nx][ny] == 0 and a[nx][ny] == 'L':
                    ch[nx][ny] = 1
                    dq.append([nx, ny, d+1])
    return d
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]   
n, m = map(int, input().split())

a = [list(map(str, input().rstrip())) for _ in range(n)]
res = -2147483647
for i in range(n):
    for j in range(m):
        if a[i][j] == 'L':
            cnt = bfs(i, j, 0)
            if cnt> res:
                res = cnt
print(res)