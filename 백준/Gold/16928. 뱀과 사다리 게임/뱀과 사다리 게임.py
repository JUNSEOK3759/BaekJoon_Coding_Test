from collections import deque, Counter
import heapq as hq
import copy
import math
import itertools

# import re
import sys
# sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)

def bfs():
    dq = deque()
    dq.append(1)
    
    while dq:
        x = dq.popleft()
        
        if x == 100:
            return a[x]
        
        for i in range(1, 7):
            next = x + i
            if next <= 100:
                if next in ladder.keys():
                    next = ladder[next]
                if next in snake.keys():
                    next = snake[next]
                if ch[next] == 0:
                    ch[next] = 1
                    a[next] = a[x] + 1
                    dq.append(next)
n, m = map(int, input().split())

ladder = {}
snake = {}

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    snake[x] = y

a = [0 for _ in range(100 + 1)]
ch = [0 for _ in range(100 + 1)]

print(bfs())