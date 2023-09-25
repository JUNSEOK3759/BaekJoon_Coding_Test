from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def sbfs(i, j, maps, n, m):
    dq = deque()
    dq.append([i, j, 0])
    ch = [[0 for _ in range(m)] for _ in range(n)]
    ch[i][j] = 1
    while dq:
        x, y, d = dq.popleft()
        if maps[x][y] == 'L':
            return d
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if -1 < nx < n and -1 < ny < m and ch[nx][ny] == 0 and maps[nx][ny] != 'X':
                ch[nx][ny] = 1
                dq.append([nx, ny, d+1])
    return -1

def ebfs(i, j, maps, n, m):
    dq = deque()
    dq.append([i, j, 0])
    ch2 = [[0 for _ in range(m)] for _ in range(n)]
    ch2[i][j] = 1
    while dq:
        x, y, d = dq.popleft()
        if maps[x][y] == 'E':
            return d
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if -1 < nx < n and -1 < ny < m and ch2[nx][ny] == 0 and maps[nx][ny] != 'X':
                ch2[nx][ny] = 1
                dq.append([nx, ny, d+1])
    return -1

                
def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    s, l = 0, 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                s = sbfs(i, j, maps, n, m)
            elif maps[i][j] == 'L':
                l= ebfs(i, j, maps, n, m)
                
    return s + l if s != -1 and l != -1 else -1