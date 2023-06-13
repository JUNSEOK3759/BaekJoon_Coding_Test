from collections import Counter
def solution(want, number, discount):
    answer = 0
    a = Counter()
    for i in range(len(want)):
        a[want[i]] = number[i]


    for i in range(len(discount)):
        x = Counter(discount[i:i+sum(number)])

        if a == x:
            answer += 1
    
    return answer