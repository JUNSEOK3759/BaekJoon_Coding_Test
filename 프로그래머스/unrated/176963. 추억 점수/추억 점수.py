def solution(name, yearning, photo):
    answer = []
    info = dict(zip(name, yearning))
    
    for people in photo:
        score = 0
        for person in people:
            if person in info:
                score += info[person]
        answer.append(score)
    return answer