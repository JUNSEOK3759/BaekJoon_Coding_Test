from collections import deque
def bfs(k, ch, wires, n):
    dq = deque()
    dq.append(k)
    visit = [0 for _ in range(n+1)]
    visit[k] = 1
    cnt = 1
    while dq:
        x = dq.popleft()
        for i in ch[x]:
            if visit[i] == 0:
                visit[i] = 1
                dq.append(i)
                cnt += 1
    return cnt

def solution(n, wires):
    answer = 2147483647
    ch = [[] for _ in range(n+1)]
    
    for x, y in wires:
        ch[x].append(y)
        ch[y].append(x)
    
    for x, y in wires:
        ch[x].remove(y)
        ch[y].remove(x)
        
        answer = min(abs(bfs(x, ch, wires, n) - bfs(y, ch, wires, n)), answer)
        
        ch[x].append(y)
        ch[y].append(x)
    
    return answer