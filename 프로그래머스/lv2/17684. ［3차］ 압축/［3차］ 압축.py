def solution(msg):
    answer = []
    a = {chr(i) : i-64 for i in range(65, 65+26)}
    lt = 0
    rt = 1
    while True:
        if rt == len(msg):
            answer.append(a[msg[lt:rt]])
            break
        if msg[lt:rt+1] not in a:
            a[msg[lt:rt+1]] = len(a) + 1
            answer.append(a[msg[lt:rt]])
            lt = rt
        rt += 1
    return answer