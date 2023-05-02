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
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a.sort()

for i in b:
    lt = 0
    rt = len(a)-1
    while lt <= rt:
        mid = (lt + rt) // 2
        if i == a[mid]:
            print(1, end = ' ')
            break
        if i > a[mid]:
            lt = mid + 1
        else:
            rt = mid -1
    else:
        print(0, end = ' ')