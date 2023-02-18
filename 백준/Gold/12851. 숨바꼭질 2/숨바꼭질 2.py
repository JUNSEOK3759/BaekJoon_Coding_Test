import sys
import heapq
from collections import deque
import itertools
# sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


    
def bfs(x, d):
    global result
    dq = deque()
    dq.append([x, d]) 
    while dq:
        x, d = dq.popleft()
        if x == k:
            result += 1
            continue
        for next in (x+1, x-1, x*2):
            if next >= 0 and next <= 100000:
                if ch[next] == 0 or ch[next] == ch[x] + 1:
                    ch[next] = ch[x] +1
                    dq.append([next, d+1])

                    

n, k = map(int, input().split())
ch =[0] * 100001
result = 0

bfs(n, 0)
print(ch[k])
print(result)