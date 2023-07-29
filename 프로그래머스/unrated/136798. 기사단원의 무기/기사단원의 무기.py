import math
def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number+1):
        result = 0
        for j in range(1, int(math.sqrt(i))+1):
            if i % j == 0:
                result += 1
                if j**2 != i:
                    result += 1
            if result > limit:
                result = power
                break
        answer += result
    return answer