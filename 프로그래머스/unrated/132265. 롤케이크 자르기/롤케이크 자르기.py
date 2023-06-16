from collections import Counter
def solution(topping):
    answer = 0
    a = Counter(topping)
    x = set()
    
    for i in topping:
        a[i] -=1
        x.add(i)
        if a[i] == 0:
            a.pop(i)
        if len(x) == len(a):
            answer += 1
    return answer