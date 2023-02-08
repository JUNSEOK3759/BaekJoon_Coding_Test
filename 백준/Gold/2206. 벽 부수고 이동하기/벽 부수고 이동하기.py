import sys
from collections import deque
import heapq as hq
import copy

# sys.stdin = open("input.txt", "rt")
# input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)

def bfs():
    dq = deque()
    dq.append([0, 0, 0])
    ch[0][0][0] = 1

    while dq:
        x, y, d = dq.popleft()
        if x == n-1 and y == m-1:
            return ch[x][y][d]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > -1 and ny > -1 and nx < n and ny < m:
                if a[nx][ny] == 0 and ch[nx][ny][d] == 0:
                    ch[nx][ny][d] = ch[x][y][d] + 1
                    dq.append([nx, ny, d])
                if d == 0 and a[nx][ny] == 1:
                    dq.append([nx, ny, 1])
                    ch[nx][ny][1] = ch[x][y][d] + 1
    return -1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
ch = [[[0] * 2 for _ in range(m)] for _ in range(n)]

print(bfs())