def solution(dirs):
    answer = set()
    move = {'U':[0, 1], 'D' : [0, -1], 'L' : [-1, 0], 'R': [1, 0]}
    x = (0, 0)
    for i in dirs:
        a = x[0] + move[i][0]
        b = x[1] + move[i][1]
        if -6 < a < 6 and -6 < b < 6:
            q = sorted([(x[0], x[1]), (a, b)])
            answer.add(tuple(q))
            x = (a, b)
    return len(answer)

