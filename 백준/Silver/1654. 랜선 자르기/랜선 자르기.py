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

def divide(mid, a):
    cnt = 0
    for i in a:
        if i != 0:
            cnt += (i // mid)
    return cnt

n, m = map(int, input().split())

a = []

for _ in range(n):
    a.append(int(input()))

if max(a) == 0:
    print(0)
    sys.exit(0)
    
lt = 1
rt = max(a)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if mid == 0:
        mid = 1
    cnt = divide(mid, a)
    
    if cnt >= m:
        res= mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
    
        