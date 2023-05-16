def solution(s):
    answer = 0
    stack = []
    
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.pop(-1)
        else:
            stack.append(s[i])
    if len(stack) == 0:
        answer = 1
    return answer