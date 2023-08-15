import math
def solution(n, k):
    answer = []
    a = [i for i in range(1, n+1)]
    
    while n != 0:
        fac = math.factorial(n-1)
        x = k // fac
        k = k % fac
        if k == 0:
            answer.append(a.pop(x-1))
        else:
            answer.append(a.pop(x))
        n -= 1
    return answer