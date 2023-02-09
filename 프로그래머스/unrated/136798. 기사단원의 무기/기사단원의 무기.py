def solution(number, limit, power):
    x = 0
    for i in range(1, number+1):
        result = 0
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                result += 1
                if j ** 2 != i:
                    result += 1
            if result > limit:
                result = power
                break
        x += result
    return x