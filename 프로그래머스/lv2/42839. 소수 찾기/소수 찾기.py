import itertools
def isPrime(x):
    answer = len(x)
    for i in x:
        if i in [0, 1]:
            answer -= 1
        for j in range(2, i):
            if i % j == 0:
                answer -=1
                break
    return answer

def solution(numbers):
    x = set()
    numbers = list(numbers)
    for i in range(1, len(numbers)+1):
        for j in list(itertools.permutations(numbers,i)):
            x.add(int(''.join(j)))
    x = list(x)
    
    return isPrime(x)