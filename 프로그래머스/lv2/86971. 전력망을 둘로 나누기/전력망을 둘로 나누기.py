from collections import deque
def solution(n, wires):
    answer = -1
    
    ch = [[] for _ in range(n+1)]
    
    for a, b in wires:
        ch[a].append(b)
        ch[b].append(a)
    
    def bfs(x):
        visit = [0 for _ in range(n+1)]
        dq = deque()
        dq.append(x)
        visit[x] = 1
        cnt = 0
        while dq:
            x = dq.popleft()
            for i in ch[x]:
                if visit[i] == 0:
                    visit[i] = 1
                    dq.append(i)
                    cnt += 1
        return cnt
    res = n
    for a, b in wires:
        ch[a].remove(b)
        ch[b].remove(a)
        
        res = min(abs(bfs(a)-bfs(b)), res)
        
        ch[a].append(b)
        ch[b].append(a)
    
    return res