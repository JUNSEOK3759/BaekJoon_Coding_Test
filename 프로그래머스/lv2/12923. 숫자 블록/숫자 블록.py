import math
def solution(begin, end):
    answer = []
    def res(x):
        k = 1
        if x == 1:
            return 0
        if x == 2:
            return 1
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                k = i
                if x // i <= 10000000:
                    return (x//i)
        else:
            return k       
    
    for i in range(begin, end + 1):
        answer.append(res(i))
    return answer