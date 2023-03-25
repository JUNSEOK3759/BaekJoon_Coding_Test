def solution(food):
    answer = ''
    for i in range(1, len(food)):
        x = food[i] // 2
        for j in range(x):
            answer += str(i)
    answer = answer + '0' + answer[::-1]
    return answer