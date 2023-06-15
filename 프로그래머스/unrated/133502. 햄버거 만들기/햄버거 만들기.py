from collections import deque
def solution(a):
    answer = 0
    a = deque(a)
    stack = []
    while a:
        stack.append(a.popleft())
        if stack and stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            answer += 1
    return answer