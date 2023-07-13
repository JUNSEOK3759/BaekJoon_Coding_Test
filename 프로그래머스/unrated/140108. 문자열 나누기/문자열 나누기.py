def solution(s):
    answer = 0
    
    cnt = [0, 0]
    compare = ''
    for i in range(len(s)):
        if compare:
            if s[i] == compare:
                cnt[0] += 1
            else:
                cnt[1] += 1
            if cnt[0] == cnt[1]:
                answer += 1
                cnt = [0, 0]
                compare = ''
        else:
            compare = s[i]
            cnt[0] += 1
    if sum(cnt) >= 1:
        answer += 1
    return answer