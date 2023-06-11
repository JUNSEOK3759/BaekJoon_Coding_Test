def solution(citations):
    answer = 0
    for i in range(1, max(citations)):
        cnt = 0
        for j in range(len(citations)):
            if citations[j]> i:
                cnt += 1
        if i >= cnt:
            return i
    return 0