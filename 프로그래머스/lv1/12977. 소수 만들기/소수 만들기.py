import itertools
import math
def isPrime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        else:
            return True
        
def solution(nums):
    answer = 0
    
    for x in list(itertools.combinations(nums, 3)):
        if isPrime(sum(x)):
            answer += 1
    

    return answer