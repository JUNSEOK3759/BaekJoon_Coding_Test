from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, maps, n, m, ch):
    dq = deque()
    dq.append([x, y])
    tot = int(maps[x][y])
    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if -1 < nx < n and -1 < ny < m and ch[nx][ny] == 0 and maps[nx][ny].isdigit():
                ch[nx][ny] = 1
                tot += int(maps[nx][ny])
                dq.append([nx, ny])
    return tot
def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    ch = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j].isdigit() and ch[i][j] == 0:
                ch[i][j] = 1
                answer.append(bfs(i, j, maps, n, m, ch))
    return sorted(answer) if answer else [-1]