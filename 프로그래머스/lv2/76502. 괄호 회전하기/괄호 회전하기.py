from collections import deque
def solution(s):
    answer = 0
    a = 0
    x = deque()
    while a < len(s):
        s = s[1 : ] + s[0]
        for i in s:
            x.append(i)
            if len(x) >= 2:
                if x[-1] == '}' and x[-2] == '{':
                    x.pop()
                    x.pop()
                elif x[-1] == ')' and x[-2] == '(':
                    x.pop()
                    x.pop()
                elif x[-1] == ']' and x[-2] == '[':
                    x.pop()
                    x.pop()
        if len(x) == 0:
            answer += 1
        else:
            x = deque()
        a+=1
    return answer