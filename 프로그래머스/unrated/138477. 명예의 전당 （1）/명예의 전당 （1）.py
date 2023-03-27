def solution(k, score):
    answer = []
    x = []
    for i in score:
        if len(x) < k:
            x.append(i)
            x.sort(reverse = True)
            answer.append(min(x))
            
        elif len(x) == k:
            if i < min(x):     
                answer.append(min(x))
            else:
                x[-1] = i
                answer.append(min(x))
                x.sort(reverse = True)
        # print(f'x : {x}, answer : {answer}, minimum : {answer[answer.index(min(x))]}')
            
    return answer