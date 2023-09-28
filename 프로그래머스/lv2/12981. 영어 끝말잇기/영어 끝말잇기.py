def solution(n, words):
    answer = [words[0]]

    for i in range(1, len(words)):
        if words[i] in answer or answer[-1][-1] != words[i][0]:
            return [i % n + 1 , i // n + 1]
        else:
            answer.append(words[i])
    return [0, 0]