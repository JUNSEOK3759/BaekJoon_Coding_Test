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

def minus(mid, a):
    res = 0
    for i in a:
        if i <= mid:
            res += i
        else:
            res += mid
    return res
n = int(input())

a = list(map(int, input().split()))

tot = int(input())

if sum(a) <= tot:
    print(max(a))
    sys.exit(0)

lt = 1
rt = max(a)
res = 2147483647

while lt <= rt:
    mid = (lt + rt) // 2
    
    cnt = minus(mid, a)
    
    if cnt <= tot:
        res = mid
        lt = mid + 1
    else:
        rt = mid -1        
print(res)
