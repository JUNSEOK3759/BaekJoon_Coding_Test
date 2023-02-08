def solution(board, moves):
    answer = []
    cnt = 0
    for i in moves:
        for j in range(len(board[0])):
            if board[j][i-1] != 0:
                answer.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(answer) > 1:
            if answer[-1] == answer[-2]:
                answer.pop()
                answer.pop()
                cnt += 2
    return cnt