import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")
# input = sys.stdin.readline

def bfs(n):
    dq = deque()
    dq.append(n)
    ch[n] = 1

    while dq:
        now = dq.popleft()
        if now == k:
            return res[k]
        for next in (now -1, now + 1, now * 2):
            if next >= 0 and next <= max:
                if ch[next] == 0:
                    ch[next] = 1
                    res[next] = res[now] + 1
                    dq.append(next)

n, k = map(int, input().split())
max = 100000
ch = [0 for _ in range(max + 1)]
res = [0 for _ in range(max + 1)]

print(bfs(n))
