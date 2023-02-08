def solution(board, moves):
    answer = []
    cnt = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                answer.append(board[j][i-1])
                board[j][i-1] = 0
                break
            else:
                continue
    x = 0
    y = 1
    while y < len(answer):
        if answer[x] == answer[y]:
            cnt += 2
            del answer[x]
            del answer[y-1]
            x = 0
            y = 1

        else:
            x += 1
            y += 1
    return cnt