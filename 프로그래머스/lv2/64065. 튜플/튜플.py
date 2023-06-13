from collections import Counter
def solution(s):
    answer = []
    x = ''
    for i in range(len(s)-1):
        if s[i].isdigit():
            x += s[i]
            if not s[i+1].isdigit():
                answer.append(int(x))
                x = ''
    counter = Counter(answer)
    counter = counter.most_common()
    x = []
    for i, j in counter:
        x.append(i)
    return x