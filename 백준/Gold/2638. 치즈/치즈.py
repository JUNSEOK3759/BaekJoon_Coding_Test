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

def bfs():
    dq = deque()
    dq.append([0, 0])
    visit = [[0 for _ in range(m)] for _ in range(n)]
    visit[0][0] = 1
    
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx > -1 and ny > -1 and nx < n and ny < m:
                if visit[nx][ny] == 0:
                    if a[nx][ny] >= 1:
                        a[nx][ny] += 1
                    else:
                        visit[nx][ny] = 1
                        dq.append([nx, ny])
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

res = 0

while True:
    
    bfs()
    flag = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] >= 3:
                a[i][j] = 0
            elif a[i][j] >= 1:
                a[i][j] = 1
                flag = 1
    res += 1   
    if flag == 0:
        break
print(res)