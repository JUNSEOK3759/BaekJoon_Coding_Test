import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

a = []

for i in range(n):
    x, y = map(str, input().split())
    a.append([int(x), y])
a.sort(key = lambda x : (x[0]))
for i in a:
    print(i[0], i[1])