import re
def solution(s, skip, index):
    alp = [chr(i) for i in range(97, 97+ 26)]
    alp = ''.join(alp)
    answer = ''
    for i in skip:
        alp = re.sub(i, '', alp)
    for i in s:
        answer += alp[(alp.index(i) + index) % len(alp)]
    return answer