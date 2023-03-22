def solution(s):
    x = s.split()
    answer = int(x[0])
    for i in range(1, len(x)):
        if x[i] == 'Z':
            x[i] = -int(x[i-1])
        answer += int(x[i])
            
    return answer