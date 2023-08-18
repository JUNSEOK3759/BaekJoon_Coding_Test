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
    
    while True:
        move = 0
        for i in range(m-1):
            for j in range(n):
                if board[i][j] != 0 and board[i+1][j] == 0:
                    board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                    move = 1
        if move == 0:
            break
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