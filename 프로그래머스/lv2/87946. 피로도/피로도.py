import itertools
def solution(k, dungeons):
    answer = 0
    for per in itertools.permutations(dungeons, len(dungeons)):
        hp = k
        cnt = 0
        for pm in per:
            if hp >= pm[0]:
                hp -= pm[1]
                cnt += 1
        if cnt > answer:
            answer = cnt
    return answer