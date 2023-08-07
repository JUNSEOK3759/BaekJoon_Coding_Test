import itertools
def solution(numbers):
    answer = set()
    numbers.sort()
    for x, y in itertools.combinations(numbers, 2):
        answer.add(x+y)
    return sorted(list(answer))