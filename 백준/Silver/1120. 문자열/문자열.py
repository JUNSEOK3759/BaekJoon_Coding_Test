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

a, b = map(str, input().split())

tot = 2147483647

for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            count += 1
    tot = min(tot, count)
print(tot)