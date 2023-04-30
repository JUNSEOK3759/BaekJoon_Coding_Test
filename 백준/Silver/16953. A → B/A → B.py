from collections import deque, Counter

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def bfs(x, d):
    dq = deque()
    dq.append([x, d])
    
    while dq:
        x, d = dq.popleft()
        
        if x == m:
            return d
        
        for next in (x * 2, int(str(x) + '1')):
            if next <= m:
                
                dq.append([next, d+1]) 
    return -1       

n, m = map(int, input().split())

print(bfs(n, 1))