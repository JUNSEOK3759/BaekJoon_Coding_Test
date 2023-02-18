import sys
import heapq
from collections import deque
import itertools
# sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def path(x):
    arr = []
    temp = x
    for _ in range(ch[x]+1):
        arr.append(temp)
        temp = check[temp]

    print(' '.join(map(str, arr[::-1])))
    
def bfs(x):
    dq = deque()
    dq.append(x) 
    while dq:
        x = dq.popleft()
        if x == k:
            print(ch[k])
            return path(x)
        for next in (x+1, x-1, x*2):
            if next >= 0 and next <= 100000:
                if ch[next] == 0:
                    ch[next] = ch[x] + 1
                    dq.append(next)
                    check[next] = x
                    

n, k = map(int, input().split())
ch =[0] * 100001
check = [0] * 100001

bfs(n)