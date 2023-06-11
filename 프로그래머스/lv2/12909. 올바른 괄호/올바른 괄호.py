def solution(s):
    stack = []
    
    for i in s:
        stack.append(i)
        while len(stack) >= 2 and stack[-1] == ')' and stack[-2] == '(':
            stack.pop()
            stack.pop()
        
    if stack:
        return False
    else:
        return True