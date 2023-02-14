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
    global ans
    ch = [[0 for _ in range(m)] for _ in range(n)] 
    
    dq = deque()
    dq.append([0, 0])
    ch[0][0] = 1
    
    cnt = 0
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > -1 and ny > -1 and nx < n and ny < m and ch[nx][ny] == 0:
                if a[nx][ny] == 0:
                    ch[nx][ny] = 1
                    dq.append([nx, ny])
                elif a[nx][ny] == 1:
                    ch[nx][ny] = 1
                    a[nx][ny] = 0
                    cnt += 1
    ans.append(cnt)
    return cnt
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
ans = []
time = 0
while True:
    time += 1   
    
    cnt = bfs()
    if cnt == 0:
        break
print(time-1)
print(ans[-2])