def check(m, n, board):
    cnt = 0
    ch = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(m-1):
        for j in range(n-1):
            a, b, c, d = board[i][j], board[i+1][j], board[i][j+1], board[i+1][j+1]
            if a == b == c == d and a != 0:
                ch[i][j], ch[i+1][j], ch[i][j+1], ch[i+1][j+1] = 1, 1, 1, 1
    
    for i in range(m):
        for j in range(n):
            if ch[i][j] == 1:
                board[i][j] = 0
                cnt += 1
    
    if cnt == 0:
        return 0
    
    for i in range(m-2, -1, -1):
        for j in range(n):
            k = i
            while 0 <= k+1 < m and board[k+1][j] == 0:
                k += 1
            if k != i:
                board[k][j] = board[i][j]
                board[i][j] = 0
    return cnt
    
def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    
    while True:
        
        x = check(m, n, board)
        if x == 0:
            break
        answer += x
    return answer