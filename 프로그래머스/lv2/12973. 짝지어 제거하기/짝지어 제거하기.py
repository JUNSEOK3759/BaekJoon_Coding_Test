def solution(s):
    answer = -1
    stack = []
    
    for i in s:
        stack.append(i)
        while len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
        
    
    return 1 if not stack else 0