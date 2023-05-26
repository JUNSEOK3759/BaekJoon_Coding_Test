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

total = []
for i in range(a):
    total.append(input().rstrip())
total = list(set(total))
total.sort(key = lambda x : (len(x), x))


for i in total:
    print(i)