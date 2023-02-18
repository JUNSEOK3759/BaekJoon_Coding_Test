import sys
import heapq
from collections import deque
import itertools
# sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n = int(input())
a = []

for i in range(n):
    heapq.heappush(a, int(input()))
res = 0
while len(a) > 1:
    x = heapq.heappop(a) + heapq.heappop(a)
    heapq.heappush(a, x)
    res += x
print(res)