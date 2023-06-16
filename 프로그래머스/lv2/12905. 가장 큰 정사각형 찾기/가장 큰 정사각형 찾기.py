def solution(board):
    dx = [1, 0, 1]
    dy = [0, 1, 1]
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i][j-1], board[i-1][j], board[i-1][j-1])+1
    answer = max(map(max, board))

    return answer ** 2