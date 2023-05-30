import sys
from collections import deque, Counter
import heapq as hq
import copy
import math
import itertools
# sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)

n = int(input())
a = []

for _ in range(n):
    a.append(input().rstrip())
a = Counter(a)
cnt = max(a.values())

tot = []
for x, y in a.items():
    if y == cnt:
        tot.append(x)
tot.sort()
print(tot[0])