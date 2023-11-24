def solution(numbers):
    answer = ''
    if sum(numbers) == 0:
        return '0'
    x = [[str(i) * 3, str(i)] for i in numbers]
    x.sort(key = lambda x: x[0], reverse = True)

    for i in x:
        answer += str(i[1])
    
    
    return answer