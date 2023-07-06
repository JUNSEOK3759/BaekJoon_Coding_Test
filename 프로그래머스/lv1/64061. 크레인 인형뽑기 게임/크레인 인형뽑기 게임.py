from collections import deque
def solution(board, moves):
    answer = 0
    moves = deque(moves)
    stack = []
    while moves:
        x = moves.popleft()-1
        for i in range(len(board)):
            if board[i][x] != 0:
                stack.append(board[i][x])
                board[i][x] = 0
                break
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2
    return answer