import sys
from collections import deque, Counter

# sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    res = 0
    for i in a:
        lt = 0
        rt = y-1
        cnt = -1
        while lt <= rt:
            mid = (lt + rt) // 2
            if i > b[mid]:
                cnt = mid
                lt = mid + 1
            else:
                rt = mid -1
        res += cnt + 1
    print(res)