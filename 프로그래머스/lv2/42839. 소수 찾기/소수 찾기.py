import math
import itertools
def solution(numbers):
    answer = set()
    num = list(numbers)
    def isPrime(x):
        if x in [0, 1]:
            return False
        if x == 2:
            return True
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        else:
            return True    
            
    for i in range(1, len(num)+1):
        for j in itertools.permutations(num,i):
            x = int(''.join(j))
            if isPrime(x):
                answer.add(x)
    return len(answer)