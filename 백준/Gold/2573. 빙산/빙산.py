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
    global n, m
    cnt = 1
    visit = [[0 for _ in range(m)] for _ in range(n)]
    visit[x][y] = 1
    
    dq = deque()
    dq.append([x, y])
    
    while dq:
        x, y = dq.popleft()
        
        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]
            
            if visit[nx][ny] == 0 and a[nx][ny] != 0:
                dq.append([nx, ny])
                visit[nx][ny] = 1
                cnt += 1
    return cnt

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ice = []

for i in range(n):
    for j in range(m):
        if a[i][j] != 0:
            ice.append([i, j])

answer = 0
cnt = 0

while ice:
    if len(ice) != bfs(ice[0][0], ice[0][1]):
        answer = cnt
        break
    
    cnt += 1
    melt = []
    for i in range(len(ice)-1, -1, -1):
        x, y = ice[i]
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if a[nx][ny] == 0:
                ch[x][y] += 1
                
        if ch[x][y] > 0:
            melt.append([x, y, i])
            
    for x, y, i in melt:
        a[x][y] -= ch[x][y]
        if a[x][y] <= 0:
            a[x][y] = 0
            ice.pop(i)
        ch[x][y] = 0

print(answer)