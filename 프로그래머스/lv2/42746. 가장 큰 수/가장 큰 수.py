def solution(numbers):
    answer = ''
    numbers.sort(key = lambda x : ((str(x)*3)[:4]), reverse = True)
    for i in numbers:
        answer += str(i)
    return str(int(answer))