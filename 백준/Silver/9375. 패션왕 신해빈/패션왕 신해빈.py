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

for _ in range(n):
    m = int(input())
    a = {}
    for _ in range(m):
        x, y = map(str, input().split())
        if y in a.keys():
            a[y] += 1
        else:
            a[y] = 1
    cnt = 1
    for i in a.values():
        cnt *= (i+1)
    
    print(cnt-1)