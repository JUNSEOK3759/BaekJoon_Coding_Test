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



n, m = map(int, input().split())
a = []

for _ in range(n):
    a.append(int(input()))
ch = [0 for _ in range(n)]
a.sort()

lt = 0
rt = a[-1]
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    now = a[0]
    cnt = 1
    
    for i in range(1, len(a)):
        if a[i] >= now + mid:
            cnt += 1
            now = a[i]
    if cnt >= m:
        lt = mid + 1
        res = mid
    else:
        rt = mid -1
print(res)