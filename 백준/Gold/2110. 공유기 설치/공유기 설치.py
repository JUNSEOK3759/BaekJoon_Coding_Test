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

def distance(mid, a, x):
    cnt = 1
    for i in a:
        if i >= x + mid:
            x = i
            cnt += 1
    return cnt
        
    
n, m = map(int, input().split())

a = []

for _ in range(n):
    a.append(int(input()))

a.sort()

lt = 0
rt = a[-1]
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    x = a[0]
    if distance(mid, a, x) >= m:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)        