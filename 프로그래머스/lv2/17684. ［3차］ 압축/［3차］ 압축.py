def solution(msg):
    answer = []
    alp = {chr(i+64) : i for i in range(1, 27)}
    n = len(msg)
    lt = 0
    rt = 1
    cnt  = 0
    while True:
        cnt += 1
        if rt == len(msg):
            answer.append(alp[msg[lt:rt+1]])
            break
        if msg[lt:rt+1] not in alp:
            alp[msg[lt:rt+1]] = len(alp) + 1
            answer.append(alp[msg[lt : rt]])
            lt = rt
        rt += 1

    return answer