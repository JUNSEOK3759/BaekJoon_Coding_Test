import itertools
def solution(number):
    answer = 0
    
    for x in list(itertools.combinations(number, 3)):
        if sum(x) == 0:
            answer += 1
    return answer