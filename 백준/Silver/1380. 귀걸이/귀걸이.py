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

qwe = 1
while True:
    n = int(input())
    res = ''
    if n == 0:
        break
    a = {}
    for i in range(n):
        a[i+1] = [str(input().rstrip())]
    for i in range(n*2-1):
        k = input().rstrip()
        x, y = k.split(' ')
        x = int(x)
        a[x].append(y)
    for y in a.values():
        if len(y) < 3:
            res = y[0]
    
    print(f'{qwe} {res}')
    qwe += 1
    