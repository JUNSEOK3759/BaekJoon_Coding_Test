def solution(msg):
    answer = []
    alpha = {chr(i): i-64 for i in range(65, 65 + 26)}
    
    lt = 0
    rt = 1
    
    while True:
        if rt == len(msg):
            answer.append(alpha[msg[lt:rt]])
            break
        if msg[lt : rt+1] not in alpha:
            answer.append(alpha[msg[lt:rt]])
            alpha[msg[lt:rt+1]] = len(alpha) + 1
            lt = rt
        rt += 1
    
    return answer

