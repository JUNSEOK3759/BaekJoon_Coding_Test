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

def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    temp = []
    temp.append([x, y])
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx > -1 and ny > -1 and nx < n and ny < n and visit[nx][ny] == 0:
                if l <= abs(a[nx][ny] - a[x][y]) <= r:
                    visit[nx][ny] = 1
                    temp.append([nx, ny])
                    dq.append([nx, ny])
    return temp

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
result = 0

while True:
    visit = [[0 for _ in range(n+1)] for _ in range(n+1)]
    flag = 0

    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                visit[i][j] = 1
                country = bfs(i, j)
                if len(country) > 1:
                    flag = 1

                    number = sum(a[x][y] for x, y in country) // len(country)
                    for x, y in country:
                        a[x][y] = number
    if flag == 0:
        break
    result += 1

print(result)