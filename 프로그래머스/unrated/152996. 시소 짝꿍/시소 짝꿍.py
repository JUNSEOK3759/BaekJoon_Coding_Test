from collections import Counter
def solution(weights):
    answer = 0
    a = Counter(weights)
    
    for i in a:
        x = a[i]
        if x > 1:
            answer += (x *(x-1)) // 2
        if i*2 in a:
            answer += x * a[i*2]
        if i * 2/3 in a:
            answer += x * a[i*(2/3)]
        if i * 3/4 in a:
            answer += x * a[i*(3/4)]
    
    return answer