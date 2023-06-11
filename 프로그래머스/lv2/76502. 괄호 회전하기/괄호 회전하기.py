from collections import deque
def solution(s):
    answer = 0
    s = deque(s)
    def asd(s):
        stack = []
        for i in s:
            stack.append(i)
            while len(stack) >= 2 and (ord(stack[-1]) == ord(stack[-2])+1 or ord(stack[-1]) == ord(stack[-2])+2):
                stack.pop()
                stack.pop()
        return stack
    cnt = 0
    while cnt < len(s):
        s.append(s.popleft())
        res = asd(s)
        if not res:

            answer += 1
        cnt += 1
        
    return answer