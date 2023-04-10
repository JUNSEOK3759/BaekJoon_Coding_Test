from collections import Counter
def solution(topping):
    answer = 0
    counter = Counter(topping)
    x = set()
    
    for i in topping:
        counter[i] -= 1
        x.add(i)
        
        if counter[i] == 0:
            counter.pop(i)
        if len(x) == len(counter):
            answer += 1
    return answer