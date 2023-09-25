dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
from collections import deque
def bfs(i, j, d, board, n, m, ch):
    dq = deque()
    dq.append([i, j, d])
    while dq:
        x, y, d = dq.popleft()
        if board[x][y] == 'G':
            return d
        for i in range(4):
            nx = x
            ny = y 
            while -1 < nx + dx[i] < n and -1 < ny + dy[i] < m and board[nx + dx[i]][ny + dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]
            if ch[nx][ny] > d+1:
                ch[nx][ny] = d+1
                dq.append([nx, ny, d+1])
    return -1

def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    ch = [[2147483647 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                ch[i][j] = 0
                return bfs(i, j, 0, board, n, m, ch)