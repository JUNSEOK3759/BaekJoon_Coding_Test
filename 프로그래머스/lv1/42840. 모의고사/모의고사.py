def solution(answers):
    answer = []
    mathLoser = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    len_answer = len(answers)
    for i in mathLoser:
        len_i = len(i)
        div = len_answer // len_i
        mod = len_answer % len_i
        compare = i*div + i[:mod]
        cnt = 0
        for j in range(len(compare)):
            if compare[j] == answers[j]:
                cnt += 1
        answer.append(cnt)
    x = max(answer)
    y = []
    for i in range(len(answer)):
        if answer[i] == x:
            y.append(i+1)
    return y