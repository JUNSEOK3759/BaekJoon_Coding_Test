import itertools
def solution(k, dungeons):
    answer = -2147483647
    
    for per in itertools.permutations(dungeons, len(dungeons)):
        hp = k
        cnt = 0
        
        for i in per:
            x, y = i
            if x <= hp:
                hp -= y
                cnt += 1
        answer = max(cnt, answer)
    return answer