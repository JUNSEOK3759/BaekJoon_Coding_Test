from collections import deque
def solution(x, y, n):
    ch = [0 for _ in range(y+10)]
    dq = deque()
    dq.append(x)
    cnt = 0
    while dq:
        k = dq.popleft()
        if k == y:
            break
        for next in (k+n, k*2, k*3):
            if next <= y:
                if ch[next] == 0:
                    ch[next] = ch[k] + 1
                    dq.append(next)
    if x == y:
        return 0
    else:
        return ch[y] if ch[y] > 0 else -1

        
        