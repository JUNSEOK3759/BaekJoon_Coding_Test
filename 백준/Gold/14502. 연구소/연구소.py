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

def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    
    while dq:
        x, y = dq.popleft()
    
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            
            if nx > -1 and ny > -1 and nx < n and ny < m:
                if ca[nx][ny] == 0:
                    ca[nx][ny] = 2
                    dq.append([nx, ny])

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

zeroA = []
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            zeroA.append([i, j])
three_A = list(itertools.combinations(zeroA, 3))
res = 0
for i in three_A:
    ca = copy.deepcopy(a)
    for j in i:
        ca[j[0]][j[1]] = 1
    
    for k in range(n):
        for l in range(m):
            if a[k][l] == 2:
                bfs(k, l)
    cnt = 0
    for k in range(n):
        for l in range(m):
            if ca[k][l] == 0:
                cnt += 1
    res = max(res, cnt)
print(res)     