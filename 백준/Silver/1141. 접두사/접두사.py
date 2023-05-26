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

a = int(input())

tot = []

for i in range(a):
    tot.append(input().rstrip())
tot.sort(key = lambda x : len(x))
cnt = 0
for i in range(len(tot)):
    for j in range(i+1, len(tot)):
        if tot[i] == tot[j][:len(tot[i])]:
            break
    else:
        cnt += 1
print(cnt)
