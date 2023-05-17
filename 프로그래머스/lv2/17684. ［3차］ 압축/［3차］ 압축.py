def solution(msg):
    answer = []
    dic = {}
    
    for i in range(65, 91):
        dic[chr(i)] = i - 64
    
    s = 0
    e = 0
    while True:
        e += 1
        if e == len(msg):
            answer.append(dic[msg[s : e]])
            break
        if msg[s: e+1] not in dic:
            dic[msg[s : e+1]] = len(dic) + 1
            answer.append(dic[msg[s : e]]) # 새로운 글자 이전까지의 딕셔너리 값
            s = e
    return answer