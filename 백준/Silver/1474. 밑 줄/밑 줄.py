import sys
from collections import deque, Counter

# sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

length = 0
a = []
for _ in range(n):
    x = str(input().rstrip())
    length += len(x)
    a.append(x)

div = (m - length) // (n-1)
mod= (m - length) % (n-1)

res = a[0]

for i in range(1, n):
    if a[i][0].islower() and mod != 0:
        mod -= 1
        res += '_' * (div+1) + a[i]
    elif i+mod == n:
        mod -= 1
        res += '_' * (div+1) + a[i]
    else:
        res += '_' * (div) + a[i]
print(res)