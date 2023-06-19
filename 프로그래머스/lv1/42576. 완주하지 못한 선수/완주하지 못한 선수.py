from collections import Counter
def solution(participant, completion):
    answer = 0
    a = Counter(participant)
    
    for i in completion:
        a[i] -= 1
        
    for i, x in a.items():
        if x == 1:
            return i