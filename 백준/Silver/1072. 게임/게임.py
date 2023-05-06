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


z = (m * 100) // n

if z >= 99:
    print(-1)
    sys.exit(0)

lt = 0
rt = n
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    
    if ((m + mid) * 100) // (n + mid) > z:
        res = mid
        rt = mid -1
    else:
        lt = mid + 1

print(res)


