import sys
from collections import deque
import heapq as hq
import copy

# sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)

def bfs():
    global cnt
    dq = set()
    dq.add((0, 0, a[0][0]))
    while dq:
        x, y, d = dq.pop()
        
        if len(d) > cnt:
            cnt = len(d)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > -1 and ny > -1 and nx < r and ny < c:
                if a[nx][ny] not in d:
                    dq.add((nx, ny, d+a[nx][ny]))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
r, c = map(int, input().split())

a = [list(map(str, input())) for _ in range(r)]

alp = [0 for _ in range(27)]
alp[ord(a[0][0]) - 64] = 1
cnt = 1
bfs()

print(cnt)