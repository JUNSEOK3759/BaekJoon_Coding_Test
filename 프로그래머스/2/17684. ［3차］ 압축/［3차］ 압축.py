def solution(msg):
    answer = []
    dic = {chr(i) : i-64 for i in range(65 , 91)}
    s, e = 0, 0
    
    while True:
        e += 1
        if len(msg) == e:
            answer.append(dic[msg[s:e]])
            break
        else:
            if msg[s:e+1] not in dic:
                dic[msg[s:e + 1]] = len(dic) + 1
                answer.append(dic[msg[s:e]])
                s = e
    
    return answer