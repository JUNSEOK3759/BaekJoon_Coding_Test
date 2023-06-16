import re
def solution(m, musicinfos):
    answer = ['(None)', 0]
    for i in musicinfos:
        x, y, z, w = i.split(',')
        for i in range(65, 73):
            w = re.sub(f'{chr(i)}#', chr(i+32), w)
            m = re.sub(f'{chr(i)}#', chr(i+32), m)
        x1, x2 = x.split(':')
        y1, y2 = y.split(':')
        x = int(x1) * 60 + int(x2)
        y = int(y1) * 60 + int(y2) 
        time = int(y-x)
        len_w = len(w)
        div = time // len_w
        mod = time % len_w
        res = w * div + w[:mod]
        if m in res:
            if len(res) > answer[1]:
                answer = [z,len(res)]
    
    return answer[0] 