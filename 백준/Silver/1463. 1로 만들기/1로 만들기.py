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

def bfs(n):
    dq = deque()
    dq.append(n)
    
    while dq:
        x = dq.popleft()
        if x == 1:
            break
        if x % 3 == 0 and a[x//3] == 0:
            dq.append(x//3)
            a[x//3] = a[x] + 1
        if x % 2 == 0 and a[x//2] == 0:
            dq.append(x//2)
            a[x//2] = a[x] + 1
        if a[x-1] == 0:
            dq.append(x-1)
            a[x-1] = a[x] + 1
                
        
n = int(input())

a = [0 for _ in range(n+1)]

bfs(n)
print(a[1])