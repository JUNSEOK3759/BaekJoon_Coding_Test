from collections import Counter
def solution(want, number, discount):
    answer = 0
    a = Counter()
    for i in range(len(want)):
        a[want[i]] = number[i]
    a = a.most_common()
    a.sort(key = lambda x : x[0])

    for i in range(len(discount)):
        x = Counter(discount[i:i+sum(number)])
        x = x.most_common()
        x.sort(key = lambda x : x[0])
        if a == x:
            answer += 1
    
    return answer