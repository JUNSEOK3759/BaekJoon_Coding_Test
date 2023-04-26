import sys
# sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline
# readline을 문자열에서 쓸 때는 rstrip()를 붙여줘라
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

a = list(map(int, input().split()))

lt = 0
rt = max(a)
res = -2147483647
while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 0
    for i in a:
        if i > mid:
            cnt += (i - mid)
    if cnt >= m:
        res = mid
        lt = mid + 1
    else:
        rt = mid -1

print(res)
    