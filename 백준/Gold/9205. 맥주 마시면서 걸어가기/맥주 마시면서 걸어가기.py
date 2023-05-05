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

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    
    while dq:
        x, y = dq.popleft()
        if abs(e1-x) + abs(e2-y) <= 1000:
            return 'happy'
        for i in range(n):
            if ch[i] == 0:
                if abs(x-cs[i][0]) + abs(y - cs[i][1]) <= 1000:
                    ch[i] = 1
                    dq.append([cs[i][0], cs[i][1]])
    return 'sad'


t = int(input())

for _ in range(t):
    n = int(input())
    s1, s2 = map(int, input().split())
    cs = []
    for _ in range(n):
        cs.append(list(map(int, input().split())))
    
    e1, e2 = map(int, input().split())
    ch = [0 for _ in range(n+1)]
    print(bfs(s1, s2))