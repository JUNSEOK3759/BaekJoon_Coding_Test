from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    answer = []
    for i in range(len(maps)):
        maps[i] = list(maps[i])
    cnt = 0
    n = len(maps)
    m = len(maps[0])
    def bfs(x, y):
        dq = deque()
        dq.append([x, y])
        cnt = int(maps[x][y])
        while dq:
            x, y = dq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if -1 < nx < n and -1 < ny < m and ch[nx][ny] == 0 and maps[nx][ny].isdigit():
                    ch[nx][ny] = 1
                    dq.append([nx, ny])
                    cnt += int(maps[nx][ny])
                    
        return cnt
    res = []
    ch = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j].isdigit() and ch[i][j] == 0:
                ch[i][j] = 1
                res.append(bfs(i, j))
    res.sort()
    
    return res if res else [-1]