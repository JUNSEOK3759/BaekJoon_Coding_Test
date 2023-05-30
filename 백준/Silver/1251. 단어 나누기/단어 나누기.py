import sys
from collections import deque
import heapq as hq
import copy
import math
import itertools
# sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)

n = list(input().rstrip())
tot = []
for i in range(1, len(n)-1):
    for j in range(i+1, len(n)):
        a = n[:i]
        b = n[i:j]
        c = n[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        tot.append(a+b+c)
answer = []
for i in tot:
    answer.append(''.join(i))

answer.sort()
print(answer[0])
        