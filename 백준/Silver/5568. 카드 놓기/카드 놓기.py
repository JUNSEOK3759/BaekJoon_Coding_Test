import sys
import heapq
from collections import deque
import itertools
# sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
k = int(input())

a = []
for _ in range(n):
    a.append(int(input()))
res = list(itertools.permutations(a, k))
for x, y in enumerate(res):
    qwe = ''
    for i in range(len(y)):
        qwe += str(y[i])
    res[x] = int(qwe)

print(len(set(res)))
