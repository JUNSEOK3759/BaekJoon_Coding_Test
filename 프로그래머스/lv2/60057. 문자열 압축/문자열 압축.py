def solution(s):
    answer = 2147483647
    if len(s) == 1:
        return 1
    len_s = len(s)
    for i in range(1,(len_s // 2) + 1):
        x = ''
        cnt = 1
        temp = s[:i]
        for j in range(i, len_s, i):
            if temp == s[j : j+i]:
                cnt += 1
            else:
                if cnt != 1:
                    x += f'{cnt}{temp}'
                else:
                    x += temp
                temp = s[j:j+i]
                cnt = 1
        if cnt != 1:
            x += f'{cnt}{temp}'
        else:
            x += temp
        answer = min(answer, len(x))
    return answer