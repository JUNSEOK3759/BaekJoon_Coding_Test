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

def bs(i):
    lt = 0
    rt = m-1
    
    while lt <= rt:
        mid = (lt + rt) // 2
        if a[mid] == i:
            return 1
        elif a[mid] < i:
            lt = mid + 1
        else:
            rt = mid -1
    return 0

n = int(input())

for _ in range(n):
    m = int(input())
    a = list(map(int, input().split()))
    a.sort()
    k = int(input())
    b = list(map(int, input().split()))
    
    for i in b:
        print(bs(i))
            
            