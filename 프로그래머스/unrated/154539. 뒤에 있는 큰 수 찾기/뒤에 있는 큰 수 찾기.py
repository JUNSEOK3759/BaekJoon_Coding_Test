def solution(numbers):
    stack = []
    answer = [-1 for _ in range(len(numbers))]
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]        
        stack.append(i)
    return answer