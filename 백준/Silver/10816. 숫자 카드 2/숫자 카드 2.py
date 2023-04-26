from collections import deque, Counter
import sys
# sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))

c = Counter(a)

for i in b:
    if i in c:
        print(c[i], end = ' ')
    else:
        print(0, end = ' ')      