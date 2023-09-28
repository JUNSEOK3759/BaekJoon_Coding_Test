def solution(s):
    answer = True
    stack = []
    for i in s:
        stack.append(i)
        if len(stack) >= 2 and stack[-2] == '(' and stack[-1] == ')':
            stack.pop()
            stack.pop()

    return True if not stack else False