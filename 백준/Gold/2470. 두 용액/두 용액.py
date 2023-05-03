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

n = int(input())

a = list(map(int, input().split()))

a.sort()

lt = 0
rt = len(a)-1
res = 2147483647
total = []
while lt < rt:
    cnt = a[lt] + a[rt]
    if abs(cnt) < res:
        total = [a[lt], a[rt]]
        res = abs(cnt)
        if res == 0:
            break
    if cnt < 0:
        lt += 1
    else:
        rt -= 1

print(total[0], total[1])