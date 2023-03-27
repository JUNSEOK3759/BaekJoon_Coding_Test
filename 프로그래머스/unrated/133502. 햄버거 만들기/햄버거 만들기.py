def solution(ingredient):
    answer = 0
    y = []
    for i in ingredient:
        y.append(i)
        if y[-4:] == [1,2,3,1]:
            answer += 1
            for _ in range(4):
                y.pop()
    return answer