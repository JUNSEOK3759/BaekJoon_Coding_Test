import sys
import heapq
from collections import deque
import itertools
import copy
# sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs(x, y, d):
    global res
    dq = set()
    dq.add((x, y, d))
    
    while dq:
        x, y, d = dq.pop()
        if len(d) > res:
            res = len(d)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx > -1 and ny > -1 and nx < r and ny < c:
                if a[nx][ny] not in d:
                    dq.add((nx, ny, d + a[nx][ny]))
                    
        
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
r, c = map(int, input().split())

a = [list(map(str, input().rstrip())) for _ in range(r)]

res = -2147483647
bfs(0, 0, a[0][0])
print(res)