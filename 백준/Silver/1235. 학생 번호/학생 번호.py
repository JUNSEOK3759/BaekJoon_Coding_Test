import sys
import re
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

for i in range(n):
    a.append(str(input().rstrip()))

x = 1
len_a = len(a[0])
while True:
    res = []
    for i in range(len(a)):
        y = a[i][-x:]
        if y in res:
            x += 1
            break
        else:
            res.append(y)
    if len(res) == len(a):
        break
print(x)