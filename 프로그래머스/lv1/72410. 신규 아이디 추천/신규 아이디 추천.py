from collections import deque
import re

def firstLastDot(x):
    if x[0] == '.':
        x.popleft()
    elif x[-1] == '.':
        x.pop()
    if x:
        return ''.join(x)
    else:
        return 'a'
    
def solution(new_id):
    n = new_id.lower()
    x = ''
    for i in n:
        if i.isdigit() or i.isalpha() or i in ['-','_','.']:
            x+= i
    x = deque(x)
    for i in range(len(x)-1):
        if x[i] == '.' and x[i+1] == '.':
            x[i] = ' '
    x = re.sub(r"\s", '', ''.join(x))
    x = firstLastDot(deque(x))
    x = x[:15]
    x = firstLastDot(deque(x))
    while len(x) < 3:
        x += x[-1]
    return x