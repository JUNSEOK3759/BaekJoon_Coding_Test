from collections import deque
def solution(board):
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def bfs(i, j):
        dq = deque()
        dq.append([i, j])
        
        while dq:
            x, y = dq.popleft()
            
            if board[x][y] == 'G':
                return ch[x][y]
            for i in range(4):
                nx = x
                ny = y
                
                while -1< nx + dx[i] < n and -1 < ny + dy[i] < m and board[nx+dx[i]][ny + dy[i]] != 'D':
                    nx += dx[i]
                    ny += dy[i]
                if ch[nx][ny] > ch[x][y] +1:
                    ch[nx][ny] = ch[x][y] + 1
                    dq.append([nx, ny])
        return -1
        
    
    n = len(board)
    m = len(board[0])
    ch = [[2147483647 for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                ch[i][j] = 0
                cnt = bfs(i, j)
    return cnt