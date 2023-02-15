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

def bfs(x):
    dq = deque()
    dq.append(x)
    ch = [0 for _ in range(100001)]
    while dq:
        x = dq.popleft()
        if x == k:
            return ch[x]
        for next in (x-1, x+1, x*2):
            if next >=0 and next < 100001:
                if ch[next] == 0:
                    if next == x*2 and next != 0:
                        dq.appendleft(next)
                        ch[next] = ch[x]
                    else:
                        dq.append(next)
                        ch[next] = ch[x] + 1
    
                    

n, k = map(int, input().split())



print(bfs(n))