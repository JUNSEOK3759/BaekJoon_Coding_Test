from collections import deque
def solution(x, y, n):
    answer = 0
    ch = [0 for _ in range(y+1)]
    if x == y:
        return 0
    def bfs(k):
        dq = deque()
        dq.append(k)
        
        while dq:
            x = dq.popleft()
            if x == y:
                break
            for next in (x + n, x * 2, x * 3):
                if next <= y and ch[next] == 0:
                    ch[next] = ch[x] + 1
                    dq.append(next)
    bfs(x)
    return ch[-1] if ch[-1] else -1