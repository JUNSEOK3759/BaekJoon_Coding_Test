import re
import math
def solution(n, k):
    answer = 0
    
    def makkk(n):
        s = ''
        while n > 0:
            s += str(n % k)
            n = n // k
        return s[::-1]

    def isPrime(i):
        if i in [0, 1]:
            return False
        if i == 2:
            return True
        for x in range(2, int(math.sqrt(i))+1):
            if i % x == 0:
                return False
        else:
            return True

    x = makkk(n)
    x = x.split('0')
    for i in x:
        if i.isdigit():
            if isPrime(int(i)):
                answer += 1
    return answer