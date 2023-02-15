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

def dfs(s, p):
    global error
    if error:
        return
    visit[s] = p
    for i in graph[s]:
        if visit[i] == 0:
            dfs(i, -p)
        elif visit[s] == visit[i]:
            error = 1
            return
k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visit = [0 for _ in range(v+1)]
    error = 0
    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    for i in range(1, v+1):
        if visit[i] == 0:
            dfs(i, 1)
        if error:
            break
    if error:
        print('NO')
    else:
        print('YES')
