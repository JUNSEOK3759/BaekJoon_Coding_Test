import re
def solution(s):
    answer = []
    s = s.split(' ')
    
    for i in s:
        if i:
            answer.append(i[0].upper() + i[1:].lower())
        else:
            answer.append(i)
    
    return ' '.join(answer)