from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, board, len_x, len_y):
    dq = deque()
    dq.append([x, y, 0])
    ch = [[0 for _ in range(len_y)] for i in range(len_x)]
    ch [x][y] = 0
    
    while dq:
        x, y, d = dq.popleft()
        
        if board[x][y] == 'G':
            return d
        
        for i in range(4):
            nx = x
            ny = y
            
            while -1 < nx + dx[i] < len_x and -1 < ny + dy[i] < len_y and board[nx + dx[i]][ny + dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]
            if ch[nx][ny] == 0:
                ch[nx][ny] = 1
                dq.append([nx, ny, d+1])
    return -1

def solution(board):
    answer = 0
    len_x = len(board)
    len_y = len(board[0])

    for i in range(len_x):
        for j in range(len_y):
            if board[i][j] == 'R':
                answer = bfs(i, j, board, len_x, len_y)
    
    
    return answer if answer else -1