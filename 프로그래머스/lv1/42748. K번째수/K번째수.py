def solution(array, commands):
    answer = []
    
    for a, b, c in commands:
        x = array[a-1:b]
        x.sort()
        answer.append(x[c-1])
    return answer