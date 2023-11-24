def solution(n, words):
    answer = [0, 0]
    
    x = [words[0]]
    
    for i in range(1, len(words)):
        if x[-1][-1] != words[i][0] or words[i] in x:
            return [i % n +1, i // n + 1]
        else:
            x.append(words[i])
    return answer