import itertools
import math

def isPrime(x):
    if x in [0, 1]:
        return 0
    elif x == 2:
        return 1
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return 0
        else:
            return 1  

def solution(numbers):
    answer = 0
    a = [i for i in numbers]
    x = set()
    for i in range(1, len(numbers)+1):
        for j in list(itertools.permutations(a, i)):
            y = int(''.join(j))
            x.add(y)
    for i in x:
        answer += isPrime(i)
        
    return answer