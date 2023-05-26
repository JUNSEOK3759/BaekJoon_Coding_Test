from collections import deque
def solution(n, wires):
    res = 2147483647
    x = [[] for _ in range(n+1)]
    for a, b in wires:
        x[a].append(b)
        x[b].append(a)
    
    def bfs(k):
        dq = deque()
        dq.append(k)
        cnt = 0
        ch = [0 for _ in range(n+1)]
        ch[k] = 1
        while dq:
            k = dq.popleft()
            for i in x[k]:
                if ch[i] == 0:
                    ch[i] = 1
                    dq.append(i)
                    cnt += 1
        return cnt
    
    for a, b in wires:
        x[a].remove(b)
        x[b].remove(a)
        
        res = min(abs(bfs(a) - bfs(b)), res)
        
        x[a].append(b)
        x[b].append(a)
        
    
    return res