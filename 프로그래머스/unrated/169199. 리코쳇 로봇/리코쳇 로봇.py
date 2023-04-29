from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def solution(a):
    def bfs(x, y, d):
        dq = deque()
        dq.append([x, y, d])
        
        while dq:
            x, y, d= dq.popleft()
            
            if a[x][y] == 'G':
                return d
            
            for i in range(4):
                nx = x
                ny = y
                while (-1 < nx + dx[i] < n and -1 < ny + dy[i] < m and a[nx + dx[i]][ny + dy[i]] != 'D'):
                    nx += dx[i]
                    ny += dy[i]
                if ch[nx][ny] > d+1:
                    ch[nx][ny] = d+1
                    dq.append([nx, ny, d+1])
        return -1
    answer = 0
    n = len(a)
    m = len(a[0])
    cnt = 0
    ch = [[2147483647 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'R':
                ch[i][j] = 0
                cnt = bfs(i, j, 0)
    return cnt 

