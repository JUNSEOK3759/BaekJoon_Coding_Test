def solution(survey, choices):
    answer = ''
    x = ['R','T','C','F','J','M','A','N']
    a = {'R' : 0, 'T' : 0,
         'C' : 0, 'F' : 0,
         'J' : 0, 'M' : 0,
         'A' : 0, 'N' : 0,}
    for i in range(len(survey)):
        if choices[i] > 4:
            a[survey[i][1]] += choices[i] - 4
        else:
            a[survey[i][0]] += 4 - choices[i]
    for i in range(0, len(x), 2):
        if a[x[i]] >= a[x[i+1]]:
            answer += x[i]
        else:
            answer += x[i+1]
    return answer