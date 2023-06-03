import re
def solution(s, skip, index):
    answer = ''
    
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        alpha = re.sub(i, '', alpha)
    for i in s:
        answer += alpha[(alpha.index(i)+ index) % len(alpha)]
    return answer