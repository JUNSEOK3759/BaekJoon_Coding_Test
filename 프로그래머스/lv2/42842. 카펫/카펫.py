def solution(brown, yellow):
    answer = []
    x = brown + yellow
    for i in range(3, x+1):
        if (x / i) % 1 == 0:
            y = x // i
            if i >= y:
                if (2*i) + (2*y) == brown + 4:
                    answer = [i, y]
    return answer