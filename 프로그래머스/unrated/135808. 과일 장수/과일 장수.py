def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    for i in range(0, len(score), m):
        x = score[i:i+m]
        len_x = len(x)
        if len_x == m:
            y = x[-1] * len_x
            answer += y
        else:
            break
        
    return answer