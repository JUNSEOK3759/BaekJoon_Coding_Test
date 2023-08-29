def solution(s):
    answer = ''
    cnt = 0
    for i in range(len(s)):
        if s[i] == ' ':
            cnt = 0
            answer += ' '
        else:
            if cnt % 2 == 0:
                answer += s[i].upper()
                cnt += 1
            else:
                cnt += 1
                answer += s[i].lower()
    return answer