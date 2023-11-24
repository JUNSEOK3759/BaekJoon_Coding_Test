from collections import deque
def bfs(x, y, n, ch):
    dq = deque()
    dq.append(x)
    while dq:
        x = dq.popleft()
        if x == y:
            return ch[x]
        for next in (x + n, x * 2, x * 3):
            if next <= y + 9 and ch[next] == 0:
                ch[next] = ch[x] + 1
                dq.append(next)
    return -1
def solution(x, y, n):
    ch = [0 for _ in range(y + 10)]
    if x == y:
        return 0
    res = bfs(x, y, n, ch)
    return res if res > 0 else -1 
