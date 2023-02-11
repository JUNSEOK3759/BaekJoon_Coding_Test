from collections import Counter
def solution(topping):
    answer = 0
    counter = Counter(topping)
    b = set()
    for i in topping:
        counter[i] -=1
        b.add(i)
        if counter[i] == 0:
            counter.pop(i)
        if len(counter) == len(b):
            answer += 1
    return answer